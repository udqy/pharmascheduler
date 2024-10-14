from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def current_schedule(request):
    # add logic to display the current schedule table
    return render(request, 'current.html')
