#!/usr/bin/env python

import argparse
import logging
from pathlib import Path

import lancedb
import torch
import transformers

DESCRIPTION = """
Embed documents in an in-process vector database.
"""

logger = logging.getLogger(__name__)


def get_args() -> argparse.Namespace:
    """
    Command-line arguments
    https://docs.python.org/3/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("--log_level", default="INFO")
    parser.add_argument("--data_dir", type=Path, help="Path of a directory containing text files", default="./data")
    parser.add_argument("--vector_db", type=Path, help="Path of the database file", default="vectors.db")
    parser.add_argument("--model", help="Embedding model name", default="nomic-ai/nomic-embed-text-v1")
    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(
        format="%(name)s:%(asctime)s:%(levelname)s:%(message)s", level=args.log_level
    )
    
    # Hugging Face transformers introduction
    # https://huggingface.co/transformers/v3.4.0/quicktour.html
       
    # The tokenizer splits text into tokens
    tokenizer = transformers.AutoTokenizer.from_pretrained(args.model)
    
    # The embedding model converts text into vectors
    model = transformers.AutoModel.from_pretrained(model_name, output_hidden_states=True)
    
    pipeline = transformers.pipeline("embedder", model=model, tokenizer=tokenizer)

    texts = list()
    # Iterate over text files
    for path in args.data_dir.glob("*.txt"):
        with path.open() as file:
            logger.info("Loaded '%s'", file.name)
            texts.append(file.read())
    

    # ?
    ids = tokenizer(texts, padding=True, return_tensors="pt")
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)
    ids = ids.to(device)	
    model.eval()


if __name__ == "__main__":
    main()
