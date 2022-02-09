import json
import spotipy
from spotipy import FailedToParseJsonFile


class Json:
    def __init__(self, json_file):
        spotipy.log.debug(f"Init JSON obj with {json_file}")
        self.file = json_file
        self.data = self.parse()

    def parse(self):
        """Parse the file as JSON"""
        with open(self.file) as json_file:
            try:
                parsed = json.load(json_file)
                json_file.close()
            except json.decoder.JSONDecodeError:
                raise FailedToParseJsonFile(f"Bad format of json in file {self.file}")
        return parsed

