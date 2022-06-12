from django.contrib import admin

from orders.views import pedido
from .models import *

# Register your models here.
admin.site.register(menu)
admin.site.register(toppings)
admin.site.register(subs)
admin.site.register(pasta)
admin.site.register(salads)
admin.site.register(Dinner)
admin.site.register(Pedido)