import json

from apex_jump.handler import lambda_handler


class DynamoSystemTest(object):
    """ Base class for tests that use `~pynamodbs` """

    mocked = False
    models = []

    @classmethod
    def setup_class(cls):
        if cls.mocked:
            for Model in cls.models:
                Model.create_table(read_capacity_units=1, write_capacity_units=1)

            while True:
                if Model.describe_table().get('TableStatus') == 'ACTIVE':
                    break

        cls.setup_class_custom()

    @classmethod
    def teardown_class(cls):
        if cls.mocked:
            for Model in cls.models:
                Model.delete_table()

        cls.teardown_class_custom()

    @classmethod
    def setup_class_custom(cls):
        pass

    @classmethod
    def teardown_class_custom(cls):
        pass


def invoke_action(action, body=None):
    body = body or {}

    return lambda_handler({
        'action': action,
        'body': body
    })


def load_test_data(filename):
    json_path = os.path.join(os.path.dirname(__file__), 'resources', filename)

    with open(json_path) as f:
        data = json.load(f)
    return data
