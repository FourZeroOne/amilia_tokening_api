import json

from datetime import datetime

from ..utils.request_handler import RequestArgs, RequestHandler


def get(data):
    request_obj = RequestHandler(data)
    args = RequestArgs(request_obj.args)

    return json.dumps({}, default=str), 200

def renew():
    pass


ROUTES = [
    {
        'url': '/api/token',
        'name': 'api__token',
        'endpoint': get,
        'methods': ['GET'],
        'auth_required': True
    }
]
