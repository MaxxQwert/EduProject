from tortoise import Tortoise, run_async, fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    username = fields.TextField()
    email = fields.TextField()
    address = fields.TextField()
    phone = fields.TextField()
    website = fields.TextField()
    company = fields.TextField()
