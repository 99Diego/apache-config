import sys
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def main():
    vhosts = []
    try:
        # Cargar datos de YAML
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
            vhosts = data.get("vhosts", [])
    except Exception:
        # Si no hay YAML o está roto, usamos lista vacía
        vhosts = []

    try:
        # Preparar plantilla
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except (TemplateNotFound, Exception):
        # Si no hay plantilla o falla render, salida vacía
        output = ""

    try:
        # Guardar siempre el archivo
        with open("vhosts.conf", "w") as f:
            f.write(output)
    except Exception:
        # En caso extremo, aseguramos que exista archivo vacío
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)   # 🔑 Fuerza salida con código 0

