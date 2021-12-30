from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from .models import Destination
from django.contrib.auth.models import User, auth
from .models import Subscriber_information
# Create your views here.

def index(request):
    dests = Destination.objects.all()
    
    return render(request,'index.html', {"dests":dests})


def checking(request,id):
    data = Destination.objects.get(id=id)
    return render(request, 'checking.html', {"res":data})
    
def detail(request):
    name = request.POST['name']
    email = request.POST['email']
    user = Subscriber_information(name=name, email=email)
    user.save()
    return redirect("/")



   
        

# def detail(request):
#     username = request.POST['username']
#     email = request.POST['email']
#     user = Subscriber_information.objects.create_user(username=username, email=email)
#     user.save();


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.Info(request, 'username is taken')
            elif User.objects.filter(email=email).exists():
                messages.Info(request, 'email is taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.Info(request, 'user created succefully')
                return redirect(request, 'login')
        else:
            messages.Info(request, 'password is not matching')
            
        return redirect("register")
        
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.Info(request, "Invalid credentials")
            return redirect(request, "login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

