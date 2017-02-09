import pytest

from lib.users import User
from common import DynamoSystemTest, invoke_action

username = 'apex-jump-bot'
email = 'foo@bar.com'

class TestUsers(DynamoSystemTest):
    mocked = True
    models = [ User ]

    class TestNewUser(object):
        @classmethod
        def setup_class(cls):
            cls.action = 'new-user'

        def setup(self):
            self.body = {
                'username': username,
                'email': email
            }

        def test_successful(self):
            res = invoke_action(self.action, self.body)
            assert User.item_exists(res['id'])

        @pytest.mark.skip(reason='Not implemented yet')
        def test_conflict(self):
            User.new(self.body)

            with pytest.raises(Exception) as e:
                invoke_action(self.action, self.body)
            assert 'Conflict' in e.value.message

        @pytest.mark.skip(reason='Not implemented yet')
        def test_bad_request(self):
            with pytest.raises(Exception) as e:
                invoke_action(self.action)
            assert 'Bad Request' in e.value.message


    class TestGetUser(object):
        @classmethod
        def setup_class(cls):
            cls.action = 'get-user'

            cls.user = User.new({
                'username': username,
                'email': email
            })

        def setup(self):
            self.body = {
                'id': self.user['id']
            }

        def test_successful(self):
            res = invoke_action(self.action, self.body)
            assert res == self.user

        def test_not_found(self):
            self.body['id'] = 'foobar'

            with pytest.raises(Exception) as e:
                invoke_action(self.action, self.body)
            assert 'Not Found' in e.value.message

        @pytest.mark.skip(reason='Not implemented yet')
        def test_bad_request(self):
            with pytest.raises(Exception) as e:
                invoke_action(self.action)
            assert 'Bad Request' in e.value.message
