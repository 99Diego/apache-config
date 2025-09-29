import yaml
from jinja2 import Environment, FileSystemLoader

try:
    # 1. Cargar los datos del archivo YAML
    with open("data.yml") as f:
        data = yaml.safe_load(f) or {}

    vhosts = data.get("vhosts", [])

    # 2. Preparar el entorno de Jinja2
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("vhosts.j2")

    # 3. Renderizar la plantilla con los datos
    output = template.render(vhosts=vhosts)

    # 4. Guardar el archivo generado
    with open("vhosts.conf", "w") as f:
        f.write(output)

    print("✅ vhosts.conf generated successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
    raise

