from unicodedata import name
from django.urls import path
from django.views import View
from django.conf import settings
from tomlkit import document
from orders import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_page, name="login"),
    path("home/", views.home, name="home"),
    path("logout/",views.logout_user, name="logout"),
    path("menu/", views.Menu, name="menu"),
    path("direction", views.direction, name="direction"),
    path("hours", views.hours, name="hours"),
    path("vs", views.vs, name="vs"),
    path("contact", views.contact, name="contact"),
    path("pedido", views.pedido, name="pedido"),
    path("aceptar_pedido", views.aceptar_pedido, name="aceptar_pedido"),
    path("delete_pedido/<int:id>", views.delete_pedido, name="delete_pedido")
   
]


#configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)