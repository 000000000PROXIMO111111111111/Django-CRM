from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpUser

#STEP 1
def home(request):
    # Check to see if logining or Posting a requesr
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging you in")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out ")
    return redirect('home')
    pass

def register_user(request):
    if request.method == 'POST':
        form = SignUpUser(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "Success, Registration Complete")
            return redirect('home')
    else:
        form = SignUpUser()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})