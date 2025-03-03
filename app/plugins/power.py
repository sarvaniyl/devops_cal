from app.commands.base import Command

class PowerCommand(Command):
    def execute(self, a, b):
        return a ** b
