from app.commands.base import Command

class SquareCommand(Command):
    def execute(self, a):
        return a * a
