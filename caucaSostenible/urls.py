from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agro-oferta", views.agro_oferta_view, name="agro-oferta"),
    path("canasta-agricola", views.canasta_agricola_view, name="canasta-agricola"),
    path("emprendimientos", views.emprendimientos_view, name="emprendimientos"),
    path("eventos", views.eventos_view, name="eventos"),
    path("gestion-items", views.gestion_items_view, name="gestion-items"),
    path("inversionistas", views.inversionistas_view, name="inversionistas"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("register", views.register, name="register"),
]
