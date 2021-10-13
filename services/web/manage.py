from flask.cli import FlaskGroup
from project import app, db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()

#skonto skonto, kreira bazu na pocetku, izbacio sam drop_all liniju, pa baza ostaje :)