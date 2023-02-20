
# Api Security

To allow the API to be used by other applications, you need to create an API bearer token. This token is used to authenticate the API requests.

## Create a Bearer Token

To create a bearer token for a user open a terminal and run the following command:

```bash
python manage.py shell
```

```py
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

username:str = 'admin'
user = User.objects.get(username=username)
token = Token.objects.create(user=user)
print(token.key)
```

Copy the token key and save it somewhere safe.
