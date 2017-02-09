from pynamodb.models import Model

from lib.common import RestfulError


class ModelCore(Model):
    @classmethod
    def new(cls, kwargs):
        item = cls(**kwargs)
        item.save()
        return item

    @classmethod
    def find(cls, kwargs):
        try:
            return cls.get(kwargs.get('id'))
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
