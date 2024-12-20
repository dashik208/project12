from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
 if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
 if form.is_valid():
    user = form.save()
    login(request, user) # Вход после регистрации
    return redirect('mainpage') # Перенаправление на главную страницу
 else:
    form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
 from django.contrib.auth.decorators import login_required
 @login_required
 def profile(request):
    return render(request, 'profile.html')
 from django.contrib.auth.views import LoginView
from . forms  import CustomAuthenticationForm
class CustomLoginView(CustomLoginView):
 template_name = 'registration/login.html'
 authentication_form = CustomAuthenticationForm
 