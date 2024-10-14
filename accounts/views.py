from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('logged_out.html')
        else:
            # Handle invalid login attempt (e.g., display error message)
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('logged_out.html')  # Redirect to your desired page after logout