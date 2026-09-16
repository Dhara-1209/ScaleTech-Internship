from unittest.mock import Mock

def get_user_name(api):
    user = api.get_user()
    return user["name"]

api = Mock()
api.get_user.return_value = {"name": "Alice"}

result = get_user_name(api)

print(result)  # Alice
api.get_user.assert_called_once_with()