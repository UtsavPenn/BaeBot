from telegram.ext import CommandHandler


class CustomCommandHandler(CommandHandler):
    def handle_update(self, update, bot):
        optional_args = {}
        message = update.message or update.edited_message

        if self.pass_args:
            optional_args['args'] = message.text.split()[1:]

        return self.callback(bot, update, **optional_args)
