from django.contrib import admin
from .models import Bill, BillDetail, Event, Investor, Product, User, Undertaking

admin.site.register(Bill)
admin.site.register(BillDetail)
admin.site.register(Event)
admin.site.register(Investor)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Undertaking)