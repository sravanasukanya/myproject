from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .PasswordManage import decrypt, encrypt
# from .forms import Userform
from .models import Users


# Create your views here.
def NewUserCreate(request):
    password = request.POST.get('pwd')
    username = request.POST.get('uid')
    if request.method == "POST":
        encr = encrypt(password,username)
        Users.objects.create(username=username, password=encr)
        dec = decrypt(encr, username)

    return render(request,'GISFAdminGISFAdmin/Registration.html')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "GISFAdmin/newuser.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "GISFAdmin/newuser.html",
                  context={"form":form})


def loginView(request):
    if request.method == 'GET':
        return render(request, 'GISFAdmin/login.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            #return redirect('mainmenu/')
            return render(request, 'GISFAdmin/mainmenu.html', {})
        else:
            return render(request, 'GISFAdmin/login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'GISFAdmin/logout.html')


def homepage(request):
    return render(request, 'GISFAdmin/home.html')


def about(request):
    return render(request,'GISFAdmin/about.html')


def mainmenu(request):
    return render(request, 'GISFAdmin/mainmenu.html')