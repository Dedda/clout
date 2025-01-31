import yaml
from jinja2 import Template

def read_config(file):
    with open(file) as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        return dict

def read_template(file):
    with open(file) as f:
        return Template(f.read())

if __name__ == "__main__":    
    config = read_config("config.yaml")
    template = read_template("compose.yaml.jinja")
    rendered = template.render(config)
    with open("compose.yaml", "w") as f:
        f.write(rendered)
    