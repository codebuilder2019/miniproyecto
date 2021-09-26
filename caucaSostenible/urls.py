from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agro-oferta", views.farming_offers_view, name="agro-oferta"),
    path("canasta-agricola", views.farming_stocks_view, name="canasta-agricola"),
    path("cart", views.cart_view, name="cart"),
    path("emprendimientos", views.undertakings_view, name="emprendimientos"),
    path("eventos", views.events_view, name="eventos"),
    path("gestion-items", views.items_management_view, name="gestion-items"),
    path("inversionistas", views.investors_view, name="inversionistas"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("register", views.register, name="register"),
]
