from django.shortcuts import render, HttpResponse, redirect

#for ML model 
import joblib

#for user login/sing-up
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

##forms library fro get data to on email direct
from django.core.mail import send_mail
from .forms import Contactforms


#import ML model
model = joblib.load('static/random_forest_regressor')

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my home page")

def prediction(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        print(age, sex, bmi, children, smoker, region)

        pred = model.predict([[age, sex, bmi, children, smoker, region]])

        print(pred)

        output = {
            "output": pred
        }
        return render(request, 'prediction.html', output)
    else:
        return render(request, 'prediction.html')    

def about(request):
    return render(request, 'about.html')

#form
def contact(request):
    if request.method=="POST":
        form = Contactforms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email Send Logic
            send_mail(
                f"New Contact Form Submission by {name}",
                f"Message: {message}\n\nFrom: {email}",
                'your_email@example.com',  # Sender Email
                ['receiver_email@example.com'],  # Receiver Email
            )
            return render(request, 'success.html', {'name': name})
    else:
        form = Contactforms()

    
    return render(request, 'contact.html', {'form': form})
    # return render(request, 'contact.html')


def success(request):
    return render(request, 'success.html')  # Render the success page after submission



def singup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Password and Confirm Password not match!!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')



        # print(uname,email,pass1,pass2)
    return render(request, 'singup.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username and Password is worng!!!!')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

