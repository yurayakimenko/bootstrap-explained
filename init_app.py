from flask import Flask

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
