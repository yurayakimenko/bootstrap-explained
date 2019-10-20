from flask import Blueprint, render_template, request, redirect, url_for
from forms import OrderForm
from models import Session, Product, OrderProduct, Order

bp = Blueprint('marketplace', __name__,
               template_folder='templates')


@bp.route('/', methods=['GET', 'POST'])
def marketplace():
    session = Session()
    products = session.query(Product).all()
    return render_template('marketplace.html', products=products)


@bp.route('/order/<int:order_id>', methods=['GET', 'POST'])
def order(order_id):
    form = OrderForm(request.form)

    session = Session()
    order = session.query(Order).get(order_id)

    if not order:
        order = Order()
        session.add(order)
        session.commit()
    # Берём список всех продуктов
    products = session.query(Product).all()
    order_products = order.order_products

    # Генерируем динамический селект для бутстреп
    choices = []
    for product in products:
        choices.append(
            (product.id, "{} - ${}"
             .format(product.name, product.price))
        )
    form.products.choices = choices

    if request.method == 'POST':
        product = session.query(Product).get(form.products.data)
        order_product = OrderProduct()
        order_product.product = product
        order_product.order = order
        session.add(order_product)
        session.commit()
        return redirect(url_for('order', order_id=order.id))

    return render_template('order_form.html', form=form, order_products=order_products)