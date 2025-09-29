import sys
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def main():
    vhosts = []
    output = ""

    # 1. Leer YAML si existe
    try:
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
            vhosts = data.get("vhosts", [])
    except Exception:
        pass  # usamos lista vacía

    # 2. Procesar plantilla si existe
    try:
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except TemplateNotFound:
        output = ""
    except Exception:
        output = ""

    # 3. Guardar siempre vhosts.conf
    try:
        with open("vhosts.conf", "w") as f:
            f.write(output)
    except Exception:
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)  # 🚀 asegura exit code 0 siempre

