# Shell scripts

I have written several shell scripts for easy managing of the experiments.

| File                   | Description                                                |
|------------------------|------------------------------------------------------------|
| `download_data.sh`     | Download the training data                                 |
| `process_data.sh`      | Save the training data to shared memory                    |
| `setup_exp.sh`         | Set up a new experiment with default settings              |
| `run_train.sh`         | Train a model                                              |
| `run_inference.sh`     | Run inference from a trained model                         |
| `run_interpolation.sh` | Run interpolation from a trained model                     |
| `run_exp.sh`           | Run an experiment (training + inference + interpolation)   |
| `rerun_exp.sh`         | Rerun an experiment (training + inference + interpolation) |
<!--

| `download_models.sh`   | Download the pretrained models                             |
-->

<br>

> Note : __execute these scripts from the root directory of the project.__

<br>

## Download the training data

```sh
# Download the training data
./scripts/download_data.sh
```

This command will download the training data to the default data directory
(`./data/`).

<br>

## Save the training data to shared memory

```sh
# Save the training data to shared memory
./scripts/process_data.sh
```

This command will store the training data to shared memory using SharedArray package.

<!--  Project description  :  Its a python package
      This is a simple python extension that lets you share numpy arrays with other processes on the same computer. It uses either shared files or POSIX shared memory as data stores and therefore should work on most operating systems.
-->

<br>

<!-- ## Download the pretrained models

```sh
./scripts/download_models.sh
```

This command will download the pretrained models to the default experiment
directory (`./exp/`).

<br> -->

## Set up a new experiment with default settings

```sh
# Set up a new experiment with default settings

./scripts/setup_exp.sh "./exp/my_experiment/" "Some notes"
```

This command will create a new experiment directory at the given path
(`"./exp/my_experiment/"`), copy the default configuration and model parameter
files to that folder and save the experiment note (`"Some notes"`) as a text
file in that folder.

<br>

## Train a model

```sh
# Train a model
./scripts/run_train.sh "./exp/my_experiment/" "0"
```

This command will look for the configuration and model parameter files in the
given experiment directory (`"./exp/my_experiment/"`) and train a model according
to the configurations and parameters on the specified GPU (`"0"`).

<br>

## Run inference from a trained model

```sh
# Run inference from a trained model

./scripts/run_inference.sh "./exp/my_experiment/" "0"
```

This command will look for the configuration and model parameter files in the
given experiment directory (`"./exp/my_experiment/"`) and run inference from the
trained model on the specified GPU (`"0"`).

<br>

## Run interpolation from a trained model

```sh
# Run interpolation from a trained model

./scripts/run_interpolation.sh "./exp/my_experiment/" "0"
```

This command will look for the configuration and model parameter files in the
given experiment directory (`"./exp/my_experiment/"`) and run inference from the
trained model on the specified GPU (`"0"`).

<br>

## Run an experiment (train + inference + interpolation)

I have written a simple wrapper for typical experiment scenario<br>&mdash; first we
train a model and then we run inference and interpolation from the trained model.
<br>
<br>
 In this case, you can simply run the following command.

```sh
# Run an experiment (train + inference + interpolation)

./scripts/run_exp.sh "./exp/my_experiment/" "0"
```

This command will look for the configuration and model parameter files in the given experiment directory (`"./exp/my_experiment/"`) and run the experiment
(train, inference and interpolation) on the specified GPU (`"0"`).

<br>

## Rerun an experiment (train + inference + interpolation)

```sh
./scripts/rerun_exp.sh "./exp/my_experiment/" "0"
```

This command will remove everything in the experiment directory except the
configuration and model parameter files and then rerun the experiment (train,
inference and interpolation) on the specified GPU (`"0"`).
