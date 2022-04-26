from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import User

# Create your views here.
def index(request):
    id_ = User.objects.values_list()[0][0]
    first_name = User.objects.values_list()[0][1]
    last_name = User.objects.values_list()[0][2]
    username = User.objects.values_list()[0][3]
    email = User.objects.values_list()[0][4]
    password = User.objects.values_list()[0][5]
    
    populate = User.populateIndex()
    
    context = {"id": id_, "first_name": first_name, "last_name": last_name, "username": username, "email": email, "populate": populate}
    
    return render(request, "dashboard/index.html", context)

def printname(request):
    if request.method == 'POST':
        current_name = request.POST.get('your_name')
        context = {"current_name" : current_name}
        return render(request, "dashboard/index.html", context)


    