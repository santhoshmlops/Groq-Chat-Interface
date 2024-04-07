# Import necessary libraries
import yaml


# Function to read yaml files
def load_config():
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)