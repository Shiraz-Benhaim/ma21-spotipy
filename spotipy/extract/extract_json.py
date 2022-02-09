import json


class Json:
    def __init__(self, json_file):
        self.file = json_file
        self.data = self.parse()

    def parse(self):
        """Parse the file as JSON"""
        with open(self.file) as json_file:
            try:
                parsed = json.load(json_file)
                json_file.close()
            except json.decoder.JSONDecodeError:
                parsed = {}
        return parsed
