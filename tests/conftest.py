import pytest
from unittest.mock import create_autospec, MagicMock

from telegram import Update, Message
from telegram.bot import Bot


@pytest.fixture(scope='module')
def bot():
    mock_bot = create_autospec(Bot, instance=True)
    return mock_bot


@pytest.fixture(scope='module')
def update():
    message = create_autospec(Message, chat_id = 101)
    update = create_autospec(Update, message=message)
    return update