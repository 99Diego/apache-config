import yaml
from jinja2 import Environment, FileSystemLoader


# ----------------------------------------
# step 1: Load YAML data
# ----------------------------------------
# Open 'data.yml' (your YAML file with vhosts definitions)
# and parse it into a Python dictionary using PyYAML
with open("data.yml") as f:
    data = yaml.safe_load(f)


# ----------------------------------------
# step 2: Setup Jinja2 environment
# ----------------------------------------
# FileSystemLoader(".") means Jinja2 will look for templates
# in the current directory (where the script is executed).
env = Environment(loader=FileSystemLoader("."))

# Load the template file called 'vhosts.j2'
template = env.get_template("vhosts.j2")


# ----------------------------------------
# step 3: Render the template
# ----------------------------------------
# Pass the YAML data to the template.
# ' data["vhosts"]' is the list of virtual hosts defined in data.yml
output = template.render(vhosts=data["vhosts"])


# ----------------------------------------
# step 4: Save the rendered config
# ----------------------------------------
# Write the rendered Apache configuration into 'vhosts.conf'
with open("vhosts.conf", "w") as f:
    f.write(output)

# confirmation message 
print("vhosts.conf generated successfully!")





