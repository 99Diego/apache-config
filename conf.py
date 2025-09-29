import yaml
from jinja2 import Environment, FileSystemLoader

def main():
    try:
        # 1. Cargar datos de YAML
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}

        vhosts = data.get("vhosts", [])

        # 2. Preparar Jinja2
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")

        # 3. Renderizar
        output = template.render(vhosts=vhosts)

        # 4. Guardar archivo
        with open("vhosts.conf", "w") as f:
            f.write(output)

        print("✅ vhosts.conf generated successfully!")

    except Exception as e:
        # Muy importante: no explotar silenciosamente
        print(f"⚠️ Error generating vhosts.conf: {e}")

if __name__ == "__main__":
    main()

