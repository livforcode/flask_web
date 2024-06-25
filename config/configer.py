import yaml


class Configer:
    def __init__(self, file_path):
        self.config_data = self._read_yaml(file_path)

    def _read_yaml(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file: {exc}")
            return {}

    def get(self, key, default=None):
        keys = key.split(".")
        data = self.config_data
        try:
            for k in keys:
                data = data[k]
            return data
        except KeyError:
            print(f"KeyError: '{key}' not found.")
            return default
        except TypeError:
            print(f"TypeError: Invalid type when accessing '{key}'.")
            return default

    def __getitem__(self, key):
        return self.get(key)

    def __repr__(self):
        return f"Config({self.config_data})"
