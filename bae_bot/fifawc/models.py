import os

from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class User(Model):
    """
    User model.
    """

    class Meta:
        table_name = os.environ.get("USERS_DYNAMODB_TABLE", "com.baebot.dev.users")

    user_id = UnicodeAttribute(hash_key=True)
    total_amount = NumberAttribute()
    reserved_amount = NumberAttribute()


class BetInfo(Model):
    """
    BetInfo Model
    """

    class Meta:
        table_name = os.environ.get("BETINFO_DYNAMODB_TABLE", "com.baebot.dev.betinfo")

    bet_id = NumberAttribute(hash_key=True)
    bet_description = UnicodeAttribute()
    bet_result_choices = ListAttribute()
    bet_deadline = UTCDateTimeAttribute()
    bet_outcome = UnicodeAttribute(null=True)

