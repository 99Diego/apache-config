# Apache VirtualHosts Generator — Python + Jinja2 + YAML 
This project automatically generates an Apache VirtualHosts configuration file (vhosts.conf) using Python, Jinja2, and YAML.
It is part of my DevOps and Infrastructure as Code (IaC) learning journey.

---

# Features
- Define multiple VirtualHosts from a simple YAML file.

- Use Jinja2 templating for dynamic and consistent Apache configs.

- Clear separation between data (data.yml) and template (vhosts.j2).

- Robust Python script (conf.py) that always produces vhosts.conf, even if data is missing.

---

## Project Structure 
```
text
apache-config/
├── conf.py        # Main Python script
├── data.yml       # VirtualHosts data in YAML
├── vhosts.j2      # Jinja2 template
├── vhosts.conf    # Generated Apache config
└── README.md      # Documentation
```

---

## Workflow
Run the tool from the command line:
```
text
data.yml  +  vhosts.j2  --(conf.py)-->  vhosts.conf
```
1 ) data.yml → stores the VirtualHost definitions.

2 ) vhosts.j2 → defines the Apache structure with dynamic variables.

3 ) conf.py → combines both using Jinja2.

4 ) vhosts.conf → final Apache configuration file.

---

### Examples
data.yml
```
yaml
vhosts:
  - server_name: www.example.com
    document_root: /var/www/example
    server_admin: admin@example.com
    directory: /usr/local/httpd/example
    allow_override: All
    options: Indexes FollowSymLinks
    order: allow,deny
    allow_from: all

  - server_name: www.test.com
    document_root: /var/www/test
    server_admin: admin@test.com
    directory: /usr/local/httpd/test
    allow_override: None
    options: None
    order: deny,allow
    allow_from: none
```
vhosts.j2
```
jinja2
{% for vhost in vhosts %}
<VirtualHost *:80>
    ServerName {{ vhost.server_name }}
    DocumentRoot {{ vhost.document_root }}
    ServerAdmin {{ vhost.server_admin }}

    {% if vhost.directory %}
    <Directory "{{ vhost.directory }}">
        AllowOverride {{ vhost.allow_override }}
        Options {{ vhost.options }}
        Order {{ vhost.order }}
        Allow from {{ vhost.allow_from }}
    </Directory>
    {% endif %}
</VirtualHost>

{% endfor %}
```
conf.py
```
python
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
```

---

# Generated Output (vhosts.conf)
```
apache
<VirtualHost *:80>
    ServerName www.example.com
    DocumentRoot /var/www/example
    ServerAdmin admin@example.com

    <Directory "/usr/local/httpd/example">
        AllowOverride All
        Options Indexes FollowSymLinks
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>

<VirtualHost *:80>
    ServerName www.test.com
    DocumentRoot /var/www/test
    ServerAdmin admin@test.com

    <Directory "/usr/local/httpd/test">
        AllowOverride None
        Options None
        Order deny,allow
        Allow from none
    </Directory>
</VirtualHost>
```

---

# Usage
1 ) Clone the repo and move into the folder:
```
bash
git clone https://github.com/<your_user>/apache-config.git
cd apache-config
```
2 ) Install dependencies:
```
bash
pip install -r requirements.txt
```
3 ) Run the generator
```
bash
python conf.py
```
4 ) Check the generated file:
```
bash
cat vhosts.conf
```

---

# Key Takeaways
- How to automate repetitive server configurations with Jinja2.
- Separation of data and logic → a basic pattern of Infrastructure as Code.
- YAML for simple, scalable, human-friendly configuration management.
- Making Python scripts robust enough not to fail with incomplete or missing data.
