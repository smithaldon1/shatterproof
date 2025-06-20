from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Event
# from app.models import User, Donation, TeamMember, Article, Match, Main

application = create_app()
migrate = Migrate(application, db)

@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Event=Event)

@application.cli.command()
def createdb():
    db.create_all()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
    # ssl_context=('cert.pem', 'key.pem')