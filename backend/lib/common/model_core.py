from pynamodb.models import Model
from pynamodb import exceptions

from lib.common import RestfulError


class ModelCore(Model):
    @classmethod
    def new(cls, kwargs):
        item = cls(**kwargs)
        item.save()
        return vars(item)['attribute_values']

    @classmethod
    def find(cls, kwargs):
        try:
            item = cls.get(kwargs.get('id'))
            return vars(item)['attribute_values']
        except exceptions.DoesNotExist:
            raise RestfulError('Not Found')

    @classmethod
    def item_exists(cls, id):
        try:
            cls.get(id)
            return True
        except exceptions.DoesNotExist:
            return False

    @classmethod
    def delete_item(cls, id):
        try:
            cls.get(id).delete()
        except exceptions.DoesNotExist:
            raise RestfulError('Not Found')
