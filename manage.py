from flask_script import Manager
from app import create_app

app=create_app()
manager=Manager(app=app)


if __name__=='__main__':
	manager.run()
