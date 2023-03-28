from django.shortcuts import render

from core.models import Contact_us, Car


# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request,'core/index.html',{'cars':cars})

def car(request):
    cars = Car.objects.all()
    return render(request,'core/car.html',{'cars':cars})

def car_single(request,id):

    car=Car.objects.get(id=id)
    cars = Car.objects.all()
    data={}
    data['car']=car
    data['cars']=cars
    return render(request,'core/car_single.html',data)

def search(request):
    query = request.GET['query']
    car = Car.objects.filter(name__icontains = query)
    context = {
        "car":car,
    }
    return render(request,'core/search.html',context)



def pricing(request):
    cars = Car.objects.all()

    return render(request,'core/pricing.html',{'cars':cars})
def add_car(request):
    return render(request,'core/add_car.html')

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
