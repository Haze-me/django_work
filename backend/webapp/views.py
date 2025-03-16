from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegistrationForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  #Save user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  #Use password1 (correct field)

            #Authenticate using the correct username and password
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'You have successfully registered! Welcome, {user.username.title()}!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please try logging in manually.')
                return redirect('home')  # Redirect to login if authentication fails

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
