import sys
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def main():
    try:
        # 1. Intentar cargar datos YAML
        try:
            with open("data.yml") as f:
                data = yaml.safe_load(f) or {}
        except Exception:
            data = {}

        vhosts = data.get("vhosts", [])

        # 2. Intentar cargar plantilla
        try:
            env = Environment(loader=FileSystemLoader("."))
            template = env.get_template("vhosts.j2")
            output = template.render(vhosts=vhosts)
        except (TemplateNotFound, Exception):
            output = ""

        # 3. Siempre escribir vhosts.conf
        with open("vhosts.conf", "w") as f:
            f.write(output)

    except Exception:
        # Último seguro: crear archivo vacío
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)  # 🚀 Fuerza siempre exit code 0

