from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dashboard.models import User
from dashboard.forms import NameForm
from dashboard.formmodeltest import UserForm

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



# examples 👇


def printname(request):
    if request.method == 'POST':
        current_name = request.POST.get('your_name')
        context = {"current_name" : current_name}
        return render(request, "dashboard/index.html", context)

def getName(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('<p>BLUUUUUU</p>')
    else:
        form = NameForm()
        
    return render(request, 'dashboard/index.html', {'form': form})
        
        
def getUserForm(request):
    if request.method == 'POST':
        form3 = UserForm(request.POST)
        if form3.is_valid():
            form3.save()
            return HttpResponse('<p>BLUUUUUU</p>')
    else:
        form3 = UserForm()
    return render(request, 'dashboard/index.html', {'form3': form3})
        