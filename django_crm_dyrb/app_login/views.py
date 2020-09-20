from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    if request.method == "POST":
        mail = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=mail, password=password)
        print(mail, password)
        if user!=None:
            login(request, user)
            return HttpResponse(f"bienvenido {user.username}")
    return render(request, 'app_login/index2.html', {})
def contacts(request):
    return render(request, 'app_login/contacts.html', {})