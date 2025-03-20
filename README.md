# Vector database on HPC

This repository contains an example embedding process and vector database for use on [Stanage high performance computing](https://docs.hpc.shef.ac.uk/en/latest/stanage/index.html#gsc.tab=0) (HPC) cluster at the University of Sheffield.

To run the embedding models, a popular option is to run an [Ollama](https://ollama.com/) server to provide models via an API. This doesn't currently work because it's incompatible with the version of GLIBC that's available on Stanage.

# Installation

1. Log into the cluster
2. Clone this repository

```bash
git clone "TODO"
```

3. Load the [Anaconda module](https://docs.hpc.shef.ac.uk/en/latest/stanage/software/apps/python.html)

```bash
module load Anaconda3
```

4. [Configure Conda](https://docs.hpc.shef.ac.uk/en/latest/stanage/software/apps/python.html) as described in the HPC documentation.
4. Create a virtual environment

```bash
conda env create --file environment.yaml
```

# Usage

From the login node, [submit the job](https://docs.hpc.shef.ac.uk/en/latest/hpc/scheduler/index.html#) to the task scheduler using `sbatch`

```bash
sbatch job.sh
```



# References

- NYU HPC [LLM on HPC](https://sites.google.com/nyu.edu/nyu-hpc/training-support/general-hpc-topics/ai-at-hpc-tips/llm-on-hpc)
- https://gist.github.com/EdwinB12/b62c8f600c8849df1059170292aa0225
