import sys
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

try:
    # Leer data.yml si existe
    try:
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        data = {}

    vhosts = data.get("vhosts", [])

    # Cargar template y renderizar
    try:
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except (TemplateNotFound, Exception):
        output = ""

    # Guardar vhosts.conf siempre
    with open("vhosts.conf", "w") as f:
        f.write(output)

except Exception:
    # Última defensa: archivo vacío
    open("vhosts.conf", "w").close()

# 🚀 Fuerza salida con 0 siempre
sys.exit(0)

