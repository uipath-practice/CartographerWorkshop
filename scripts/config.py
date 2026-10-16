"""Configuration and Azure OpenAI client setup."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import AzureOpenAI

# Project paths
SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
DOCS_ROOT = PROJECT_ROOT / "docs"
CONTEXT_DIR = SCRIPTS_DIR / "context"
VECTOR_STORE_PATH = CONTEXT_DIR / "vector_store.json"

# Image processing constants
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
METADATA_SUFFIX = ".metadata.json"
SKIP_DIRS = {"assets/images"}

# Load environment
load_dotenv(SCRIPTS_DIR / ".env")

AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
AZURE_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY", "")
AZURE_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")
AZURE_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-5.4")
AZURE_EMBEDDING_DEPLOYMENT = os.environ.get(
    "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small"
)


def validate_config() -> None:
    """Validate that required environment variables are set."""
    missing = []
    if not AZURE_ENDPOINT:
        missing.append("AZURE_OPENAI_ENDPOINT")
    if not AZURE_API_KEY:
        missing.append("AZURE_OPENAI_API_KEY")
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        print(f"Create scripts/.env from scripts/.env.example and fill in your credentials.")
        sys.exit(1)


def get_openai_client() -> AzureOpenAI:
    """Create and return an Azure OpenAI client."""
    validate_config()
    return AzureOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        api_version=AZURE_API_VERSION,
    )
