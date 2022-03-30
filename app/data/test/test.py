import time

list = []


class Post:
    def __init__(self):
        self.time = time.time


for i in range(0, 10):
    list.append(Post)

for i in range(0, len(list)):
    list.pop(list.index(Post))
    print(len(list))

print(list)
