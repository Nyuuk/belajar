from flask import Flask

def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'adnan0987'

    # import Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from .get import geta as get_blueprint
    app.register_blueprint(get_blueprint)
    from .post import app as post_blueprint
    app.register_blueprint(post_blueprint)
    from .put import app as put_blueprint
    app.register_blueprint(put_blueprint)
    from .delete import app as delete_blueprint
    app.register_blueprint(delete_blueprint)
    return app
