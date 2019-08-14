from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def welcome(request):
        return redirect("/login")

def registration(request):
        errors = Company.objects.company_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request,value)
                return redirect('/')
        else:
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                Company.objects.create(name=request.POST["name"],address=request.POST['address'],email=request.POST['email'],password=hash1)
                company= Company.objects.last()
                request.session['company_id']= company.id
                return redirect('/dashboard')

def dashboard(request):
        # if 'user_id' not in request.session:
        #         return redirect('/')
        # else: 
                products = Product.objects.all()
                vehicles = Vehicle.objects.all()
                context = {
                        'products': products,
                        'vehicles': vehicles
                }
                return render(request, "eyeStock_app/dashboard.html", context)

def login(request):
        return render(request, "eyeStock_app/login.html")

def process_login(request):
        errors = Company.objects.login_validator(request.POST)
        if len(errors) > 0:
                for key, value in errors.items():
                        messages.error(request, value)
                return redirect('/')
        else:
                company_list = Company.objects.filter(email=request.POST['email'])
                if bcrypt.checkpw(request.POST['password_log'].encode(),company_list[0].password.encode()):
                        request.session['company_id'] = company_list[0].id
                        return redirect('/dashboard')

def checkout(request):
        return render(request, 'eyeStock_app/product_checkout.html')

def products(request):
        return render(request, "eyeStock_app/products.html")

def add_product(request):
        Product.objects.create(
                product_name = request.POST['product_name'], 
                barcode_number= request.POST['barcode_number'],
                description = request.POST ['description']
                )
        return redirect('/dashboard')

def add_vehicle(request):
        Vehicle.objects.create(
                year = request.POST['year'],
                make = request.POST['make'],
                model = request.POST['model'],
                vin = request.POST['vin'],
                stock_number = request.POST['stock_number']
        )
        vehicle = Vehicle.objects.last()
        context = {
                'vehicle':vehicle,
        }
        return redirect('/dashboard', context)

def employee_form(request):
        return render(request, "eyeStock_app/employee_form.html")

def add_employee(request):
        Employee.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST ['last_name'],
                employee_address = request.POST['employee_address'],
                phone_number = request.POST['phone_number'],
                employee_email = request.POST ['employee_email']
        )
        employee = Employee.objects.last()
        request.session['employee_id'] = employee.id
        return redirect('/employee_file')

def employee_list(request):
        return render(request, "eyeStock_app/employee_list.html")

def logout(request):
        request.session.clear()
        return redirect('/')