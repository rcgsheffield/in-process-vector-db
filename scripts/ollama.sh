# Ollama on stanage
# The GLIBC version is too old

ssh stanage
srun --pty bash -i

# Setup ollama
# https://github.com/ollama/ollama/blob/main/docs/linux.md
# Get program files
wget https://ollama.com/download/ollama-linux-amd64.tgz
mkdir ollama
tar --directory=ollama --extract --gzip --file ollama-linux-amd64.tgz

module load GCC
# $ ldd --version | head -n 1
#ldd (GNU libc) 2.17

~/ollama/bin/ollama --version
# /users/cs1jsth/ollama/bin/ollama: /lib64/libm.so.6: version `GLIBC_2.27' not found 
