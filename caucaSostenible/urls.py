from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("register", views.register, name="register"),
]
"""
    path("", views.index, name="index"),    
    path("catalog/add", views.addCatalogView, name="add-catalog"),
    path("catalog/add-record", views.addCatalog, name="add-catalog-record"),
    path("catalog/<int:catalogId>", views.catalogView, name="catalog"),
    path("catalogs", views.catalogsView, name="catalogs"),
    path("product/add", views.addProductView, name="add-product"),
    path("product/add-record", views.addProduct, name="add-product-record"),
    path("product/<int:productId>", views.productView, name="product"),
    path("delete-account", views.deleteAccount, name="delete-account"),
    path("user-profile", views.userProfile, name="user-profile"),
"""