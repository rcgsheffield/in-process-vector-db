#!/bin/bash

# This is a SLURM job script that uses an embedding model
# to populate an in-process vector database.

# Stop on errors
set -e

# Options
data_dir="./data"
url="https://ia600202.us.archive.org/15/items/thecompleteworks00100gut/pg100.txt"
env_name="embedding-env"
env_file="environment.yaml"

module load Anaconda3

# Activate virtual environment
# https://docs.hpc.shef.ac.uk/en/latest/stanage/software/apps/python.html
conda env update --quiet --name "$env_name" --file "$env_file" --prune
source activate "$env_name"

mkdir --parents ./data
wget "$url" --quiet -O "$data_dir/data.txt"

conda --version
python --version
which python

# Run embedding script
python embed.py --data_dir="$data_dir"
