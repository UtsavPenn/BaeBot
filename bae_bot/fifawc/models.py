import os

from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model


class User(Model):
    """
    User model.
    """

    class Meta:
        table_name = os.environ.get("USERS_DYNAMODB_TABLE", "com.baebot.dev.users")

    first_name = UnicodeAttribute(hash_key=True)
    total_amount = NumberAttribute()
    reserved_amount = NumberAttribute()



