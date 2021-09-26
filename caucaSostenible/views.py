from django.urls import reverse
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bill, BillDetail, Event, Investor, Product, User, Undertaking

def cart_view(request):
    bill = Bill.objects.get(user=request.user)
    
    if bill:
        billDetails = BillDetail.objects.all().filter(bill=bill)
    else:
        bill = Bill(user=request.user, total=0)
        bill.save()
    
    return render(request, "general/cart.html", {"bill": bill, "billDetails": billDetails})

def farming_offers_view(request):
    products = Product.objects.all().exclude(discount=0)

    return render(request, "general/agro_oferta.html", {"products": products})

def farming_stocks_view(request):
    products = Product.objects.all()

    return render(request, "general/canasta_agricola.html", {"products": products})

def events_view(request):
    events = Event.objects.all()

    return render(request, "general/eventos.html", {"events": events})

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("maintenance"))
    else:
        return HttpResponseRedirect(reverse("login"))

def investors_view(request):
    investors = Investor.objects.all()
    
    return render(request, "general/inversionistas.html", {"investors": investors})

def items_management_view(request):
    return render(request, "general/gestion_items.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "general/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "general/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def maintenance(request):
    return render(request, "general/maintenance.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "general/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "general/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "general/register.html")

def undertakings_view(request):
    undertakings = Undertaking.objects.all()
    
    return render(request, "general/emprendimientos.html", {"undertakings": undertakings})
