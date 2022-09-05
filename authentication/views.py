from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rithik import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import employee
from .models import electrician
from .models import plumber
from .models import renovator
from .models import carpenter
from .models import house_keeper
from .models import AC_service
from .models import TV_service

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def about_page(request):
    return render(request,"authentication/aboutpage.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "your account has been successfully created ! We have sent you a confirmation email, please confirm your email in order to activate your account.")
        
        #welcome email
        
        subject = "welcome to QUICK QUICK - Django login"
        message = "hello "+myuser.first_name+"!!\n"+"Welcome to the quick quick\n"+"we have also sent a verification email to your email please confirm your account.\n\n Thank you\n "
        from_email= settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        #Email confirmation
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Quick Quick - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')

    


    return render(request,"authentication/signup.html") 


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname' : fname})
            

        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')



def service(request):
    result = employee.objects.all()
    return render(request,"authentication/service.html",{'result':result})

def ac(request):
    result = AC_service.objects.all()
    return render(request,"authentication/ac.html",{'result':result})

def tv(request):
    result = TV_service.objects.all()
    return render(request,"authentication/tv.html",{'result':result})

def renovators(request):
    result = renovator.objects.all()
    return render(request,"authentication/renovator.html",{'result':result})

def plumbers(request):
    result = plumber.objects.all()
    return render(request,"authentication/plumbers.html",{'result':result})

def electricians(request):
    result = electrician.objects.all()
    return render(request,"authentication/electrician.html",{'result':result})

def carpenters(request):
    result = carpenter.objects.all()
    return render(request,"authentication/carpenter.html",{'result':result})

def housekeeper(request):
    result = house_keeper.objects.all()
    return render(request,"authentication/housekeeper.html",{'result':result})

