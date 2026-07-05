import json
import os
from jinja2 import Environment, FileSystemLoader

def main():
    # 1. Wczytanie definicji danych
    with open("generator/interface.json", "r") as f:
        data_definition = json.load(f)

    # 2. Konfiguracja Jinja2
    env = Environment(loader=FileSystemLoader("generator/templates"))
    template = env.get_template("serializer.py.j2")

    # 3. Renderowanie kodu
    generated_code = template.render(data_definition)

    # 4. Zapis do pliku docelowego
    os.makedirs("app", exist_ok=True)
    with open("app/generated_codec.py", "w") as f:
        f.write(generated_code)
    
    print("Sukces: Kod serializatora został wygenerowany w app/generated_codec.py")

if __name__ == "__main__":
    main()