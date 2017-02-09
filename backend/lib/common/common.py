from uuid import uuid4
from jsonschema import validate, exceptions


class RestfulError(ValueError):
    pass


def get_uuid():
    return str(uuid4())


def load_schema(schema):
    definitions = 'schema/{}.yml'.format(schema)
    with open(definitions) as stream:
        data = yaml.load(stream)
    return data


def validate_request(data, schema):
    """Validates event payload with yaml schema"""
    try:
        assert validate(data, load_schema(schema)) is None
    except (exceptions.ValidationError, exceptions.SchemaError) as e:
        logging.error('invalid request')
        logging.error(e)
        raise RestfulError('Bad Request: Missing or incorrect parameters')
