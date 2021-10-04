from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bill, BillDetail, Event, Investor, Product, User, Undertaking
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def add_to_cart(request, productId):
    if request.method == "GET":
        try:
            bill = Bill.objects.get(user=request.user)
            product = Product.objects.get(id=productId)
            billDetail = BillDetail(bill=bill, product=product)
            billDetail.save()

            calculateBillTotal(bill)

            return JsonResponse({
                "message": "Product added"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Product not added"
            }, status=406)
    elif request.method == "DELETE":
        try:
            bill = Bill.objects.get(user=request.user)
            product = Product.objects.get(id=productId)
            billDetail = BillDetail.objects.get(bill=bill, product=product).delete()

            calculateBillTotal(bill)

            return JsonResponse({
                "message": "Product removed"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Product not removed"
            }, status=406)

def calculateBillTotal(bill):    
    billTotal = 0
    billDetails = BillDetail.objects.all().filter(bill=bill)

    for aBillDetail in billDetails:
        billTotal+= aBillDetail.product.price - aBillDetail.product.discount

    bill.total = billTotal
    bill.save()

def cart_view(request):
    bill = Bill.objects.get(user=request.user)
    
    if bill:
        billDetails = BillDetail.objects.all().filter(bill=bill)

    return render(request, "general/cart.html", {"bill": bill, "billDetails": billDetails})

@csrf_exempt
@login_required
def events(request, eventId):
    if request.method == "DELETE":
        try:
            event = Event.objects.get(id=eventId)

            if event:
                event.delete()

            return JsonResponse({
                "message": "Event removed"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Event not removed"
            }, status=406)

def events_crud_view(request):
    events = Event.objects.all()

    return render(request, "general/eventos_crud.html", {"events": events})

def events_view(request):
    events = Event.objects.all()

    return render(request, "general/eventos.html", {"events": events})

def farming_offers_view(request):
    products = Product.objects.all().exclude(discount=0)
    billDetails = None

    if request.user.id != None:
        bill = Bill.objects.get(user=request.user)
        
        if bill:
            billDetails = serializers.serialize("json", BillDetail.objects.all().filter(bill=bill))

    return render(request, "general/agro_oferta.html", {"products": products, "billDetails": billDetails})

def farming_stocks_view(request):
    products = Product.objects.all()
    billDetails = None

    if request.user.id != None:
        bill = Bill.objects.get(user=request.user)
        
        if bill:
            billDetails = serializers.serialize("json", BillDetail.objects.all().filter(bill=bill))

    return render(request, "general/canasta_agricola.html", {"products": products, "billDetails": billDetails})

def index(request):
    if request.user.is_authenticated:
        return render(request, "general/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))

@csrf_exempt
@login_required
def investments(request, investmentId):
    if request.method == "DELETE":
        try:
            investment = Investment.objects.get(id=investmentId)

            if investment:
                investment.delete()

            return JsonResponse({
                "message": "Investment removed"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Investment not removed"
            }, status=406)

def investors_crud_view(request):
    investors = Investor.objects.all()

    return render(request, "general/inversionistas_crud.html", {"investors": investors})

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

@csrf_exempt
@login_required
def products(request, productId):
    if request.method == "POST":
        try:
            name = request.POST["Nombre"]
            price = request.POST["Precio"]
            discount = request.POST["Descuento"]
            description = request.POST["Descripcion"]
            imgURL = request.POST["ImagenURL"]

            product = Product(name=name, price=price, discount=discount, description=description, imgURL=imgURL)
            product.save()
            
            return JsonResponse({
                "message": "Product added"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Product not added"
            }, status=406)
    if request.method == "DELETE":
        try:
            product = Product.objects.get(id=productId)

            if product:
                billDetails = BillDetail.objects.all().filter(product=product)

                for billDetail in billDetails:
                    bill = billDetail.bill
                    bill.total -= product.price - product.discount
                    bill.save()
                    billDetail.delete()

                product.delete()

            return JsonResponse({
                "message": "Product removed"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Product not removed"
            }, status=406)

def products_crud_view(request):
    products = Product.objects.all()

    return render(request, "general/productos_crud.html", {"products": products})

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

            bill = Bill(user=request.user, total=0)
            bill.save()
        except IntegrityError:
            return render(request, "general/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "general/register.html")

@csrf_exempt
@login_required
def undertakings(request, undertakingId):
    if request.method == "DELETE":
        try:
            undertaking = Undertaking.objects.get(id=undertakingId)

            if undertaking:
                undertaking.delete()

            return JsonResponse({
                "message": "Undertaking removed"
            }, status=201)
        except IntegrityError:
            return JsonResponse({
                "message": "Undertaking not removed"
            }, status=406)

def undertakings_crud_view(request):
    undertakings = Undertaking.objects.all()

    return render(request, "general/emprendimientos_crud.html", {"undertakings": undertakings})

def undertakings_view(request):
    undertakings = Undertaking.objects.all()
    
    return render(request, "general/emprendimientos.html", {"undertakings": undertakings})
