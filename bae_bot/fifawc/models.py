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

class BetsHistory(Model):
    """
    BetsHistory model.
    """

    class Meta:
        table_name = os.environ.get("BETS_HISTORY_DYNAMODB_TABLE", "com.baebot.dev.bets_history")

    bet_id = UnicodeAttribute(hash_key=True)
    event_id = NumberAttribute()
    user_id = UnicodeAttribute()
    bet_amount = NumAttribute()
    result = UnicodeAttribute()
    bet_processed = NumAttribute()


class EventInfo(Model):
    """
    EventInfo Model
    """

    class Meta:
        table_name = os.environ.get("EVENTINFO_DYNAMODB_TABLE", "com.baebot.dev.eventinfo")

    event_id = NumberAttribute(hash_key=True)
    event_description = UnicodeAttribute()
    event_result_choices = ListAttribute()
    event_deadline = UTCDateTimeAttribute()
    event_outcome = UnicodeAttribute(null=True)

