<!-- MuseGAN
Warning: this version is no longer maintained

MuseGAN is a project on music generation. In essence, we aim to generate polyphonic music of multiple tracks (instruments) with harmonic and rhythmic structure, multi-track interdependency and temporal structure. To our knowledge, our work represents the first approach that deal with these issues altogether.

The models are trained with Lakh Pianoroll Dataset (LPD), a new multi-track piano-roll dataset, in an unsupervised approach. The proposed models are able to generate music either from scratch, or by accompanying a track given by user. Specifically, we use the model to generate pop song phrases consisting of bass, drums, guitar, piano and strings tracks.

Sample results are available here. -->



# Music Production

This is a project on music generation / Production. In a nutshell, we aim to generate polyphonic music of multiple tracks (instruments). The proposed models are able to generate music either from scratch, or by accompanying a track given by the user.

We train the model with training data collected from
[Lakh Pianoroll Dataset](https://colinraffel.com/projects/lmd/) to generate pop song phrases consisting of bass, drums, guitar, piano and strings tracks.
<!-- The Lakh MIDI dataset is a collection of 176,581 unique MIDI files -->


<!-- Decribe the piano roll and its representation  : https://salu133445.github.io/lakh-pianoroll-dataset/representation


   The above pianoroll visualizations are produced using
   Pypianoroll ->  https://salu133445.github.io/pypianoroll/
   which is a pyhthon library.
    *  handle piano-rolls of multiple tracks with metadata
    *  utilities for manipulating piano-rolls
    *  save to and load from .npz files using efficient sparse matrix format
    *  parse from and write to MIDI files

    visualization page of this library : https://salu133445.github.io/pypianoroll/visualization.html



    .npz -> NpzFile is used to load files in the NumPy .npz data archive format.
     It assumes that files in the archive have a .npy extension, other files are ignored.
 -->


<!-- discribe about teh pop music genere : https://en.wikipedia.org/wiki/Pop_music -->
<!-- Sample results are available
[here](https://salu133445.github.io/musegan/results). -->

#
## __Install dependencies__

- Using pip
  ```sh
  # Install the dependencies
  pip install -r requirements.txt
  ```

#
## __Prepare training data__

> The training data is collected from
[Lakh Pianoroll Dataset]() (LPD), a new multitrack pianoroll dataset¡.

```sh
# Download the training data
./scripts/download_data.sh

# Store the training data to shared memory
./scripts/process_data.sh
```
<!--
You can also download the training data manually
([train_x_lpd_5_phr.npz](https://docs.google.com/uc?export=download&id=12Z440hxJSGCIhCSYaX5tbvsQA61WD_RH)). -->


#
## __Scripts__

I have written Several shell scripts for easy managing the experiments. (See [here](scripts/README.md) for scripts detailed documentation.)

<!-- > __Below we assume the working directory is the repository root.__ -->

> Note : __execute these scripts from the root directory of the project.__


<br>

1. Command to set up a new experiment with default settings.

   ```sh
   # Set up a new experiment
   ./scripts/setup_exp.sh "./exp/my_experiment/" "Some notes on my experiment"
   ```
    <br>

2. You can modify the configuration and model parameter files for experimental settings.

    <br>

3. You can either train the model:

     ```sh
     # Train the model
     ./scripts/run_train.sh "./exp/my_experiment/" "0"
     ```
   __OR__   .. run the experiment (training + inference + interpolation):

     ```sh
     # Run the experiment
     ./scripts/run_exp.sh "./exp/my_experiment/" "0"
     ```

   __OR__   .. after training you can do __inference__  AND __interpolatioln__ separately.

   => Perform inference from a trained model:

   ```sh
   # Run inference from a pretrained model
   ./scripts/run_inference.sh "./exp/default/" "0"
   ```

   => Perform interpolation from a trained model:

   ```sh
   # Run interpolation from a pretrained model
   ./scripts/run_interpolation.sh "./exp/default/" "0"
   ```


<!--
### __Use pretrained models__

1. Download pretrained models

   ```sh
   # Download the pretrained models
   ./scripts/download_models.sh
   ```

   You can also download the pretrained models manually
   ([pretrained_models.tar.gz](https://docs.google.com/uc?export=download&id=1gySWtj5_19jGrwIYd_YT11bide8DJHyN)). -->


<!--

#
## Sample Results

Some sample results can be found in `./exp/` directory.

- [`sample_results.tar.gz`](https://docs.google.com/uc?export=download&id=1OUWv581V9hWPiPGb_amXBdJX-_qoNDi9) (54.7 MB):
  sample inference and interpolation results
- [`training_samples.tar.gz`](https://docs.google.com/uc?export=download&id=1sr68zXGUrX-eC9FGga_Kl58YxZ5R2bc4) (18.7 MB):
  sample generated results at different steps -->



#
## __Papers__

__Convolutional Generative Adversarial Networks with Binary Neurons for
Polyphonic Music Generation__<br>
Hao-Wen Dong and Yi-Hsuan Yang<br>
Retrieval Conference_ (ISMIR), 2018.<br>
<!-- [[website](https://salu133445.github.io/bmusegan)]

   ==> This is some binary-musgan
        and its a follow up project for musegan.
    It gives some model and shit check it out too

-->

[paper](link from my site's pdf folder -> for that i need to might need to change and host the site )]
<!-- [[paper](link from my site's pdf folder -> for that i need to might need to change and host the site )]

    NEED TO HOST  this
-->

<!-- [[slides(short)](change this pdf or slide its just the  ppt version of the above paper)]

   NEED TO HOST  this too
   or share it using hte google slides or something
-->


<!-- [[code](https://github.com/salu133445/bmusegan)] '

this is  the code for the binary-musegan
this whole paper is for the binary muse-gan implementation
  -->











<!-- This paper is followed by the project muse-gan -->
__MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic
Music Generation and Accompaniment__<br>
Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang and Yi-Hsuan Yang,

[[paper]( hos this pdf or ppt on the github pdf folder or
you can share it by google or microsoft slides ro exle)]

[[code](https://github.com/prashant-kr-314/Music-Production)]

<!-- [[website]( host if on github.io)] -->

<!-- [[paper]( hos this pdf or ppt on the github pdf folder or
you can share it by google or microsoft slides ro exle)]
-->

<!-- [[slides](https://salu133445.github.io/musegan/pdf/musegan-aaai2018-slides.pdf)] -->







__MuseGAN: Demonstration of a Convolutional GAN Based Model for Generating
Multi-track Piano-rolls__<br>
Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang and Yi-Hsuan Yang
<br>


[[paper](link from my github project)]