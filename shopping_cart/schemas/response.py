from bson import json_util
import json


def response_message(type_info, data):
    return json.loads(json_util.dumps({type_info: data}))