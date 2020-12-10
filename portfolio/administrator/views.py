from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

# Create your views here.
def admin_login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'administrator/index.html', {'forms': form})
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse('logged in')
        return render(request, 'administrator/index.html', {'forms': form, 'error':'Username and Password Incorrect'})
