from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dashboard import loginform
from dashboard.models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from dashboard.loginform import UserForm
from django.contrib.auth.backends import BaseBackend

# from dashboard.forms import NameForm
# from dashboard.formmodeltest import UserForm


# Create your views here.
def index(request):
    # user_id = User.objects.get(pk=user_id)
    
    # id_ = Users.objects.values_list()[0][0]
    # first_name = Users.objects.values_list()[0][1]
    # last_name = Users.objects.values_list()[0][2]
    # username = Users.objects.values_list()[0][3]
    # email = Users.objects.values_list()[0][4]
    # password = Users.objects.values_list()[0][5]
    
    # # populate = Users.populateIndex()

    # current_name = request.POST.get('username')
    # context = {"id": id_, "first_name": first_name, "last_name": last_name, "username": username, "email": email, "current_name": current_name}
    # return render(request, "dashboard/index.html", context)
    




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
        # return render(request,'dashboard/index.html', context)
    else:
        return HttpResponse('try again')
    



# examples 👇

def loginForm(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse('<p>Welcome</p>' + ' ' + '<p>' + username + '</p>')
        else:
            return HttpResponse('try again')
    else:
        form = UserForm()

    return render(request, "registration/login.html", {'form': form})
    

def authUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        context = {'user': username}
        return render(request, "registration/login.html", context)
    else:
        return HttpResponse('try again')






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