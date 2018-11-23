from django.shortcuts import render
from .models import Neighborhood, User, Business, Update
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def landing(request):
    current_user = request.user
    updates = Update.get_all()
    return render(request,'landing.html',{'updates':updates})
