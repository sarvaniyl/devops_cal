import multiprocessing

class Invoker:
    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        self.commands[name] = command

    def execute(self, name, *args):
        if name in self.commands:
            return self.commands[name](*args)
        return "Unknown command."

    def execute_async(self, name, *args):
        process = multiprocessing.Process(target=self.execute, args=(name, *args))
        process.start()
