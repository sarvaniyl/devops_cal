from app.invoker import Invoker
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.database import Database

class REPL:
    def __init__(self):
        self.invoker = Invoker()
        self.database = Database()

        # Register commands
        self.invoker.register("add", AddCommand().execute)
        self.invoker.register("subtract", SubtractCommand().execute)
        self.invoker.register("multiply", MultiplyCommand().execute)
        self.invoker.register("divide", DivideCommand().execute)
        self.invoker.register("menu", self.show_menu)

    def show_menu(self):
        print("Available commands:", ", ".join(self.invoker.commands.keys()))

    def start(self):
        print("Welcome to the interactive calculator! Type 'exit' to quit.")
        while True:
            command = input("> ").strip().split()
            if not command:
                continue

            cmd_name = command[0].lower()
            args = list(map(float, command[1:])) if len(command) > 1 else []

            if cmd_name == "exit":
                break
            if cmd_name == "history":
                print(self.database.get_history())
                continue

            if cmd_name in self.invoker.commands:
                result = self.invoker.execute(cmd_name, *args)
                print(result)
                self.database.save_command(" ".join(command))
            else:
                print("Unknown command.")

if __name__ == "__main__":
    REPL().start()
