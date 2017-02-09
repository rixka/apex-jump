from pynamodb.attributes import UnicodeAttribute

from common import ModelCore
from common import get_uuid, get_now_time


class User(ModelCore):
    class Meta:
        table_name = 'apex_jump_users'
        host = 'http://localhost:8080'

    id = UnicodeAttribute(hash_key=True, default=get_uuid)
    username = UnicodeAttribute()
    email = UnicodeAttribute()

    jwt = UnicodeAttribute(null=True)
    created_at = UnicodeAttribute(default=get_now_time)
    updated_at = UnicodeAttribute(default=get_now_time)
