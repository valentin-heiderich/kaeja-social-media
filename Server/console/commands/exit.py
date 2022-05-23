import Server.classes.posts as posts
import Server.data.basicData as bD


def code_exit():
    print("Shutting down...")
    bD.running = False
    posts.save_posts()
    print("Shutdown complete.")
