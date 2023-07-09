from tortoise import Model, fields

class Email(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    email = fields.CharField(320, unique=True)