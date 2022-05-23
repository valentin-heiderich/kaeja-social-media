import Server.data.basicData as bD

import pickle


def load_posts():
    with open(bD.dataBase, 'rb') as file:
        bD.posts = pickle.load(file)


def save_posts():
    with open(bD.dataBase, 'wb') as file:
        print(bD.posts)
        pickle.dump(bD.posts, file)
