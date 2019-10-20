import marketplace
import admin
from settings import CONFIG, DEBUG
from init_app import app
from admin.views import admin



def main():
    app.secret_key = "some secret key"
    app.register_blueprint(marketplace.views.bp)
    admin.init_app(app)
    # app.register_blueprint(admin.views.bp)
    app.run(CONFIG['web']['host'], port=CONFIG['web']['port'], debug=DEBUG)


if __name__ == '__main__':
    main()
