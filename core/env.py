from pathlib import Path
from dotenv import load_dotenv
import os

def load_environment() -> None:
    """
    Load environment variables in two steps:

    1. Base .env (optional) – can define ENV_MODE and shared defaults.
    2. Environment-specific .env.<ENV_MODE> (e.g. .env.dev, .env.staging, .env.prod).

    ENV_MODE defaults to 'dev' if not set.
    """
    project_root = Path(__file__).resolve().parents[1]

    # 1) Base .env (if present)
    base_env = project_root / ".env"
    load_dotenv(dotenv_path=base_env, override=False)

    # 2) Environment-specific file
    env_mode = os.getenv("ENV_MODE", "dev")
    env_file = project_root / f".env.{env_mode}"
    load_dotenv(dotenv_path=env_file, override=True)