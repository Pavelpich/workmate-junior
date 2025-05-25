import json
from .base_output import OutputFormatter


class JsonOutput(OutputFormatter):
    def render(self, data: dict) -> str:
        return json.dumps(data, indent=2)
