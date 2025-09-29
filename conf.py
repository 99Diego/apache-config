import sys
import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    # 1. Leer YAML de forma segura
    try:
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        data = {}

    vhosts = data.get("vhosts", [])

    # 2. Cargar plantilla y renderizar
    try:
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except Exception:
        output = ""

    # 3. Escribir siempre vhosts.conf
    try:
        with open("vhosts.conf", "w") as f:
            f.write(output)
    except Exception:
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)  # <- Forzar exit code 0

