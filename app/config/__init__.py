import json
import os
from operator import itemgetter

def get_config():
    path = os.path.dirname(__file__)
    with open(path + '/config.json', 'r') as content_file:
        content = content_file.read()
        data = json.loads(content)
        # get all services sorted by priority level
        return sorted(data["services"], key=itemgetter('priority'), reverse=True)
