from rest_framework_api_key.models import APIKey


def get_apikey():
    key = APIKey.objects.create_key(name="AnonumysUser")
    print(key)