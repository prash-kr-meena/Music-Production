"""This file contains functions for loading and preprocessing pianoroll data.
"""
import logging
import numpy as np
import tensorflow as tf
from musegan.config import SHUFFLE_BUFFER_SIZE, PREFETCH_SIZE
LOGGER = logging.getLogger(__name__)

# --- Data loader --------------------------------------------------------------
def load_data_from_npy(filename):
    """Load and return the training data from a npy file."""
    return np.load(filename)

#  ==>  What is an NPZ file?  <===
# The NPZ file type is primarily associated with nProtect by INCA Internet Co, Ltd.
#   nProtect is a new Web-based anti-hacking & anti-virus tool designed to protect PC terminals from being infected by viruses or hacking tools. A game client which uses GameGuard downloads .NPZ files and extracts them for game hacking protection. NPZ files are mostly GameGuard updates located at the game server's host. When downloading a game client with GameGuard, first the GameGuard initializes itself, checks for updates, and if any, downloads NPZ files from the remote host (probably the game server's host).

# How to open an NPZ file?
# You need a suitable software like nProtect from INCA Internet Co, Ltd. to open an NPZ file. Without proper software you will receive a Windows message "How do you want to open this file?" (Windows 10) or "Windows cannot open this file" (Windows 7) or a similar Mac/iPhone/Android alert. If you cannot open your NPZ file correctly, try to right-click or long-press the file. Then click "Open with" and choose an application.


# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

# NpzFile(fid)

# A dictionary-like object with lazy-loading of files in the zipped archive provided on construction.

# NpzFile is used to load files in the NumPy .npz data archive format. It assumes that files in the archive have a .npy extension, other files are ignored.

# The arrays and file strings are lazily loaded on either getitem access using obj['key'] or attribute lookup using obj.f.key. A list of all files (without .npy extensions) can be obtained with obj.files and the ZipFile object itself using obj.zip.

def load_data_from_npz(filename):
    """Load and return the training data from a npz file (sparse format)."""
    with np.load(filename) as f:
        data = np.zeros(f['shape'], np.bool_)
        data[[x for x in f['nonzero']]] = True
    return data

def load_data(data_source, data_filename):
    """Load and return the training data."""
    if data_source == 'sa':
        import SharedArray as sa
        return sa.attach(data_filename)
    if data_source == 'npy':
        return load_data_from_npy(data_filename)
    if data_source == 'npz':
        return load_data_from_npz(data_filename)
    raise ValueError("Expect `data_source` to be one of 'sa', 'npy', 'npz'. "
                     "But get " + str(data_source))

# --- Dataset Utilities -------------------------------------------------------
def random_transpose(pianoroll):
    """Randomly transpose a pianoroll with [-5, 6] semitones."""
    semitone = np.random.randint(-5, 6)
    if semitone > 0:
        pianoroll[:, semitone:, 1:] = pianoroll[:, :-semitone, 1:]
        pianoroll[:, :semitone, 1:] = 0
    elif semitone < 0:
        pianoroll[:, :semitone, 1:] = pianoroll[:, -semitone:, 1:]
        pianoroll[:, semitone:, 1:] = 0
    return pianoroll

def set_pianoroll_shape(pianoroll, data_shape):
    """Set the pianoroll shape and return the pianoroll."""
    pianoroll.set_shape(data_shape)
    return pianoroll

def set_label_shape(label):
    """Set the label shape and return the label."""
    label.set_shape([1])
    return label

# --- Sampler ------------------------------------------------------------------
def get_samples(n_samples, data, labels=None, use_random_transpose=False):
    """Return some random samples of the training data."""
    indices = np.random.choice(len(data), n_samples, False)
    if np.issubdtype(data.dtype, np.bool_):
        sample_data = data[indices] * 2. - 1.
    else:
        sample_data = data[indices]
    if use_random_transpose:
        sample_data = np.array([random_transpose(x) for x in sample_data])
    if labels is None:
        return sample_data
    return sample_data, labels[indices]

# --- Tensorflow Dataset -------------------------------------------------------
def _gen_data(data, labels=None):
    """Data Generator."""
    if labels is None:
        for item in data:
            if np.issubdtype(data.dtype, np.bool_):
                yield item * 2. - 1.
            else:
                yield item
    else:
        for i, item in enumerate(data):
            if np.issubdtype(data.dtype, np.bool_):
                yield (item * 2. - 1., labels[i])
            else:
                yield (item, labels[i])

def get_dataset(data, labels=None, batch_size=None, data_shape=None,
                use_random_transpose=False, num_threads=1):
    """Create  and return a tensorflow dataset from an array."""
    if labels is None:
        dataset = tf.data.Dataset.from_generator(
            lambda: _gen_data(data), tf.float32)
        if use_random_transpose:
            dataset = dataset.map(
                lambda pianoroll: tf.py_func(
                    random_transpose, [pianoroll], tf.float32),
                num_parallel_calls=num_threads)
        dataset = dataset.map(lambda pianoroll: set_pianoroll_shape(
            pianoroll, data_shape), num_parallel_calls=num_threads)
    else:
        assert len(data) == len(labels), (
            "Lengths of `data` and `lables` do not match.")
        dataset = tf.data.Dataset.from_generator(
            lambda: _gen_data(data, labels), [tf.float32, tf.int32])
        if use_random_transpose:
            dataset = dataset.map(
                lambda pianoroll, label: (
                    tf.py_func(random_transpose, [pianoroll], tf.float32),
                    label),
                num_parallel_calls=num_threads)
        dataset = dataset.map(
            lambda pianoroll, label: (set_pianoroll_shape(
                pianoroll, data_shape), set_label_shape(label)),
            num_parallel_calls=num_threads)

    dataset = dataset.shuffle(SHUFFLE_BUFFER_SIZE).repeat().batch(batch_size)
    return dataset.prefetch(PREFETCH_SIZE)
