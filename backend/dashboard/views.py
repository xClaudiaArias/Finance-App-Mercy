from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from dashboard.models import Users
from dashboard import loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from dashboard.loginform import UserForm
from django.contrib.auth.backends import BaseBackend
from dashboard.register import RegisterUser

# from dashboard.forms import NameForm
# from dashboard.formmodeltest import UserForm


# Create your views here.
def index(request):
    current_name = request.POST.get('username')
    context = {"name": current_name}
    return HttpResponse("<p>Hello</p>")
    

def register(request):
    if request.method == 'POST':
        register_form = RegisterUser(request.POST)
        if register_form.is_valid():
            # return HttpResponse('<p>success</p>')
            return HttpResponseRedirect('registration/register.html')
        else:
            return HttpResponse('try again')
    else:
        register_form = RegisterUser()        
    
    return render(request, "registration/register.html", {'register_form': register_form})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # username = request.POST['username']
    # password = request.POST['password']
    user = Users.objects.get(username=username, password=password)
    # user2 = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user, backend='django.template.backends.django.DjangoTemplates')
        context = {'user': username}
        return HttpResponse('welcome, ' + username)
        # return HttpResponseRedirect("dashboard/index")
        # return render(request,'dashboard/index.html', context)
    else:
        return HttpResponse('try again')



def loginForm(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse('<p>Welcome</p>')
        else:
            return HttpResponse('try again')
    else:
        form = UserForm()

    return render(request, "registration/login.html", {'form': form})
    



# examples 👇



# def printname(request):
    # if request.method == 'POST':
    #     current_name = request.POST.get('your_name')
    #     context = {"current_name" : current_name}
    #     return render(request, "dashboard/index.html", context)

# def getName(request):
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponse('<p>BLUUUUUU</p>')
    # else:
    #     form = NameForm()
        
    # return render(request, 'dashboard/index.html', {'form': form})
        
        
# def getUserForm(request):
    # if request.method == 'POST':
    #     form3 = UserForm(request.POST)
    #     if form3.is_valid():
    #         form3.save()
    #         return HttpResponse('<p>BLUUUUUU</p>')
    # else:
    #     form3 = UserForm()
    # return render(request, 'dashboard/index.html', {'form3': form3})
        
        
        
        
# Creating a form to change an existing article.
# >>> article = Article.objects.get(pk=1)
# >>> form = ArticleForm(instance=article)





    # user_id = User.objects.get(pk=user_id)
    
    # id_ = User.objects.values_list()[0][0]
    # first_name = User.objects.values_list()[0][1]
    # last_name = User.objects.values_list()[0][2]
    # username = User.objects.values_list()[0][3]
    # email = User.objects.values_list()[0][4]
    # password = User.objects.values_list()[0][5]
    
    # populate = Users.populateIndex()
    
        # context = {"id": id_, "first_name": first_name, "last_name": last_name, "username": username, "email": email, "current_name": current_name}