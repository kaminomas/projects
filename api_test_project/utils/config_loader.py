import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)
    base_url = config["base_url"]