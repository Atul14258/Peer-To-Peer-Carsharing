from django.shortcuts import render

from core.models import Contact_us, Car


# Create your views here.
def index(request):
    return render(request,'core/index.html')

def car(request):
    cars = Car.objects.all()
    return render(request,'core/car.html',{'cars':cars})

def car_single(request):
    return render(request,'core/car_single.html')

def car_book(request):
    return render(request,'core/car_book.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact_us(
            name = request.POST.get('name'),
            email=request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request, 'core/contact.html')
