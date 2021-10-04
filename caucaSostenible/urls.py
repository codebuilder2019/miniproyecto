from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agro-oferta", views.farming_offers_view, name="agro-oferta"),
    path("canasta-agricola", views.farming_stocks_view, name="canasta-agricola"),
    path("cart", views.cart_view, name="cart"),
    path("cart/product/<int:productId>", views.add_to_cart, name="addToCart"),
    path("emprendimientos", views.undertakings_view, name="undertakingsView"),
    path("emprendimientos/<int:undertakingId>", views.undertakings, name="undertakings"),
    path("emprendimientos-crud", views.undertakings_crud_view, name="undertakingsCrud"),
    path("eventos", views.events_view, name="eventsView"),
    path("eventos/<int:eventId>", views.events, name="events"),
    path("eventos-crud", views.events_crud_view, name="eventsCrud"),
    path("gestion-items", views.items_management_view, name="gestion-items"),
    path("inversionistas", views.investors_view, name="investorsView"),
    path("inversionistas/<int:investorId>", views.investors, name="investors"),
    path("inversionistas-crud", views.investors_crud_view, name="investorsCrud"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("productos/<int:productId>", views.products, name="products"),
    path("productos-crud", views.products_crud_view, name="productsCrud"),
    path("register", views.register, name="register"),
]
