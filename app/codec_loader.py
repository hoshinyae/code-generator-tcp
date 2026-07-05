from pathlib import Path
import sys

from generator.generate import render_codec

ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"


def ensure_generated_codec() -> Path:
    render_codec()
    app_dir_str = str(APP_DIR)
    if app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)
    return APP_DIR / "generated_codec.py"
