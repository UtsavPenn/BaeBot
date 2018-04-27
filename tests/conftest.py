import pytest
from unittest.mock import create_autospec, MagicMock

from telegram import Update, Message
from telegram.bot import Bot


@pytest.fixture(scope='module')
def bot():
    mock_bot = create_autospec(Bot, instance=True)
    return mock_bot

@pytest.fixture(scope='module')
def event():
    var = {'resource': '/baebot',
                  'body': '{"update_id":518409986,\n"message":{"message_id":66,"from":{"id":419476177,"is_bot":false,"first_name":"Tharun","last_name":"Reddy","username":"tharunb","language_code":"en"},"chat":{"id":419476177,"first_name":"Tharun","last_name":"Reddy","username":"tharunb","type":"private"},"date":1524848654,"text":"/start","entities":[{"offset":0,"length":7,"type":"bot_command"}]}}',
                  'isBase64Encoded': False}
    return var

@pytest.fixture(scope='module')
def update():
    message = create_autospec(Message, chat_id = 101)
    update = create_autospec(Update, message=message)
    return update