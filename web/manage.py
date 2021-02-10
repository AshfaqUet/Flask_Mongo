from flask_script import Manager, Server, Shell
from web import create_app, db
from web.config import WebConfig

app = create_app()
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("runserver", Server(host="127.0.0.1", port=WebConfig.PORT))
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
