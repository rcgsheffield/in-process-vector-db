#!/usr/bin/env python

import argparse
import logging

from langchain_core.documents import Document
from langchain.document_loaders import UnstructuredURLLoader
from langchain_ollama import OllamaEmbeddings


DESCRIPTION = """
TODO
"""

DOCUMENT_URLS: set[str] = {
    "https://shakespeare.mit.edu/macbeth/full.html",
    "https://shakespeare.mit.edu/lll/full.html",
    "https://shakespeare.mit.edu/allswell/full.html",
}

logger = logging.getLogger(__name__)


def get_args() -> argparse.Namespace:
    """
    Command-line arguments
    https://docs.python.org/3/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("--log_level", default=logging.WARNING)
    parser.add_argument("-e", "--embedding_model", default="nomic-embed-text:latest")
    return parser.parse_args()


def load_documents(urls: set[str]) -> list[Document]:
    """
    Load documents from URLs

    https://python.langchain.com/docs/concepts/document_loaders/
    """
    loader = UnstructuredURLLoader(urls=urls)
    return loader.load()


def main():
    args = get_args()
    logging.basicConfig(
        format="%(name)s:%(asctime)s:%(levelname)s:%(message)s", level=args.log_level
    )

    documents = load_documents(DOCUMENT_URLS)

    embeddings = OllamaEmbeddings(model=args.embedding_model)


if __name__ == "__main__":
    main()
