from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # chech the logged in user
    if request.method == 'POST':
        #Username = request.POST['username']
        #password = request.POST['password']
        username = request.POST.get('username', None)  # Returns None instead of raising an error
        password = request.POST.get('password', None)
        
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            
            #then we have to redirect to the page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
            return render(request, 'home.html')



# this func will be used, if we want to use any seperate page for login
#def login_view(request):
 #   pass


def logout_view(request):
   logout(request)
   messages.success(request, 'You are logged out')
   return redirect('home')
