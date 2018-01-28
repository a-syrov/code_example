import json
import os

from .models import BashQuote, BashAbyssQuote

module_dir = os.path.dirname(__file__)  # get current directory

bash_json = os.path.join(module_dir, 'utils/json_dump/quotes.json')
abyss_json = os.path.join(module_dir, 'utils/json_dump/abyss_quotes.json')

def load_json(file):
    with open(file) as data_file:
        return json.loads(data_file.read())

def create_bash_quote(file):
    data = load_json(file)
    print(data)

if __name__ == '__main__':
    create_bash_quote(bash_json)
