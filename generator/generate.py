import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ROOT_DIR = Path(__file__).resolve().parent.parent
INTERFACE_PATH = ROOT_DIR / "generator" / "interface.json"
TEMPLATE_DIR = ROOT_DIR / "generator" / "templates"
OUTPUT_PATH = ROOT_DIR / "app" / "generated_codec.py"


def render_codec(interface_path: Path = INTERFACE_PATH, template_dir: Path = TEMPLATE_DIR, output_path: Path = OUTPUT_PATH) -> None:
    with interface_path.open("r", encoding="utf-8") as f:
        data_definition = json.load(f)

    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template("serializer.py.j2")
    generated_code = template.render(data_definition)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.write(generated_code)

    print(f"Sukces: Kod serializatora został wygenerowany w {output_path}")


def main() -> None:
    render_codec()


if __name__ == "__main__":
    main()