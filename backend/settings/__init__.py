from dotenv import load_dotenv
from pathlib import Path

base_path = Path(__file__).parent / ".." / ".."
load_dotenv(base_path.resolve())
