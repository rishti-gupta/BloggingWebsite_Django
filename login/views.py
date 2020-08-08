from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login:home')
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def home_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                pass
        else:
            form = BlogForm()
        return render(request, "index.html", context={"form": form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "register.html", context)


def logout_request(request):
    return redirect("login:login")
