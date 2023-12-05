from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordChangeForm
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'custom_password_change.html'  # Twój własny plik szablonu
    success_url = reverse_lazy('success_url')  # Możesz ustawić URL przekierowania po pomyślnym zmienieniu hasła


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out."))
    return redirect('/')

def custom_password_reset(request):
    return auth_views.PasswordChangeView.as_view(form_class=CustomPasswordChangeForm)(request)
