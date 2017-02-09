import pytest

from lib.users import User
from common import DynamoSystemTest, invoke_action


class TestNewUser(DynamoSystemTest):
    mocked = True
    models = [ User ]

    @classmethod
    def setup_class_custom(cls):
        cls.action = 'new-user'
        cls.username = 'apex-jump-bot'

    def setup(self):
        self.body = {
            'username': self.username,
            'email': 'foo@bar.com'
        }

    def test_successful(self):
        user = invoke_action(self.action, self.body)
        assert User.item_exists(user.id)
