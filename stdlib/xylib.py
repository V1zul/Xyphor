import os
import requests
import threading

class XyphorStandardLibrary:
    """Standard Library for Xyphor programming language."""

    def read_file(self, filename):
        """Reads content from a file."""
        with open(filename, "r") as f:
            return f.read()

    def write_file(self, filename, content):
        """Writes content to a file."""
        with open(filename, "w") as f:
            f.write(content)

    def fetch_url(self, url):
        """Fetches data from a URL."""
        response = requests.get(url)
        return response.text
