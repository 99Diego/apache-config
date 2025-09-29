import sys
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def main():
    vhosts = []
    output = ""

    try:
        with open("data.yml") as f:
            data = yaml.safe_load(f) or {}
            vhosts = data.get("vhosts", [])
    except Exception:
        pass

    try:
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("vhosts.j2")
        output = template.render(vhosts=vhosts)
    except (TemplateNotFound, Exception):
        output = ""

    try:
        with open("vhosts.conf", "w") as f:
            f.write(output)
    except Exception:
        open("vhosts.conf", "w").close()

if __name__ == "__main__":
    main()
    sys.exit(0)
