from datetime import datetime
from pynamodb import exceptions
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute

from common import get_uuid
from common import ModelCore


class User(ModelCore):
    class Meta:
        table_name = 'apex_jump_users'
        host = 'http://localhost:8080'

    id = UnicodeAttribute(hash_key=True, default=get_uuid)
    username = UnicodeAttribute()
    email = UnicodeAttribute()

    jwt = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)
