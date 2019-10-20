from extensions import admin
from flask_admin.contrib.sqla import ModelView
from models import Session, Product, Order, OrderProduct

admin.add_view(ModelView(Product, Session))
admin.add_view(ModelView(OrderProduct, Session))
admin.add_view(ModelView(Order, Session))

# bp = Blueprint('admin', __name__,
#                url_prefix='/admin',
#                template_folder='templates')
