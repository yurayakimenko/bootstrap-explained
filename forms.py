from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators


class OrderForm(FlaskForm):

    name = StringField('Имя получателя', [validators.Length(max=30)])
    products = SelectField('Выберите товар')