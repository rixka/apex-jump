import os
import sys
import json

root_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(root_path, "../"))
sys.path.append(os.path.join(root_path, "../vendored"))

from lib.users import User
from lib.common import RouterCore


class Router(RouterCore):
    actions = {
        'new-user': {
            'run':User.new
        },
        'get-user': {
            'run': User.find
        }
    }

lambda_handler = Router()
