import Server.console.commands.exit as exit
import Server.classes.posts as posts


class console:
    def __init__(self):
        self.listen()

    def listen(self):
        while True:
            command = input(">> ")
            if command == "exit":
                exit.code_exit()
            if command == "save":
                posts.save_posts()
            else:
                print("Command not found")
