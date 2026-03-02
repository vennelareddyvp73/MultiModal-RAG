"""
template.py

Generates a production-grade modular structure
for a Multimodal RAG system.

Run inside your existing Multimodal-RAG root folder.
"""

from pathlib import Path


PROJECT_STRUCTURE = [

    # ==========================
    # CONFIG
    # ==========================
    "configs/logging.yaml",
    "configs/settings.yaml",

    # ==========================
    # SOURCE ROOT
    # ==========================
    "src/__init__.py",
    "src/config/settings.py",

    # ==========================
    # INGESTION PIPELINE (Offline)
    # ==========================
    "src/ingestion/__init__.py",
    "src/ingestion/pipeline.py",
    "src/ingestion/pdf_parser.py",
    "src/ingestion/image_extractor.py",
    "src/ingestion/image_describer.py",
    "src/ingestion/chunker.py",

    # ==========================
    # EMBEDDING LAYER
    # ==========================
    "src/embedding/__init__.py",
    "src/embedding/base.py",
    "src/embedding/gemini_embedding.py",
    "src/embedding/embedding_factory.py",

    # ==========================
    # VECTOR STORE LAYER
    # ==========================
    "src/vectorstore/__init__.py",
    "src/vectorstore/base.py",
    "src/vectorstore/chroma_store.py",
    "src/vectorstore/vectorstore_factory.py",

    # ==========================
    # RETRIEVAL LAYER
    # ==========================
    "src/retrieval/__init__.py",
    "src/retrieval/retriever.py",

    # ==========================
    # LLM LAYER
    # ==========================
    "src/llm/__init__.py",
    "src/llm/base.py",
    "src/llm/gemini_llm.py",
    "src/llm/llm_factory.py",

    # ==========================
    # RAG QUERY PIPELINE (Online)
    # ==========================
    "src/rag/__init__.py",
    "src/rag/query_pipeline.py",
    "src/rag/prompt_builder.py",

    # ==========================
    # UTILITIES
    # ==========================
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/exceptions.py",

    # ==========================
    # TESTS
    # ==========================
    "tests/__init__.py",
    "tests/test_ingestion.py",
    "tests/test_retrieval.py",
    "tests/test_rag_pipeline.py",

    # ==========================
    # DEVOPS
    # ==========================
    "docker/Dockerfile",
    "docker/docker-compose.yml",

    "scripts/run_ingestion.py",
    "scripts/run_server.py",

    # ==========================
    # DOCS
    # ==========================
    "docs/architecture.md",
]


def create_file(path: Path):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        print(f"Created: {path}")
    else:
        print(f"Skipped: {path}")


def generate():
    base_path = Path.cwd()

    for file_path in PROJECT_STRUCTURE:
        create_file(base_path / file_path)
        

if __name__ == "__main__":
    generate()