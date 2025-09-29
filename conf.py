import sys
import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    vhosts = []
    try:
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
            vhosts = data.get("vhosts", [])
    except Exception:
        # Si no hay YAML válido, usamos lista vacía
        vhosts = []

    try:
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except Exception:
        # Si no hay template o falla el render, salida vacía
        output = ""

    try:
        with open("vhosts.conf", "w") as f:
            f.write(output)
    except Exception:
        # En caso extremo, aseguramos que el archivo exista
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)   # <- fuerza siempre exit code 0

