from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from dashboard import incomeform
from dashboard.models import Users, Income
from dashboard import loginform
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from dashboard.loginform import UserForm
from dashboard.incomeform import AddIncome
from django.contrib.auth.backends import BaseBackend
from dashboard.register import RegisterUser
from django.views.decorators.csrf import csrf_exempt
from django.views import View 

# Create your views here.

def index(request):
    current_name = request.POST.get('username')
    context = {"name": current_name}
    return render(request, "dashboard/base.html", context)
    

def register(request):
    if request.method == 'POST':
        register_form = RegisterUser(request.POST)
        if register_form.is_valid():
            register_form.save()
            password = register_form.cleaned_data.get('password1')
            new_user = Users(first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), username = request.POST.get('username'), email = request.POST.get('email'), password = password)
            new_user.save()
            # return HttpResponse('<p>Good Job</p>')
            return redirect('/login/')
    else:
        register_form = RegisterUser()      
    
    return render(request, "registration/register.html", {'register_form': register_form})

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user, backend='django.template.backends.django.DjangoTemplates')
        return redirect('/accounts/profile/')
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

# create a new view for the form 
# THIS IS PROFILE 
# def profile(request):
#     current_name = request.user.username
#     user_name = request.user
#     c_id = request.user.id
    
    
#     context = {"name": current_name, 'user_name': user_name, "c_id":c_id}
#     return render(request, "dashboard/profile.html", context)
    

# def incomeForm(request):
#     if request.method == 'POST':
#         add_income_form = AddIncome(request.POST)
#         if add_income_form.is_valid():
#             user_id = request.user.id
#             new_income = Income(income_name = request.POST.get('income_name'), deposit = request.POST.get('deposit'), current_user_id = user_id)
#             new_income.save()     
#             return redirect('/accounts/profile/')
            
#     else:
#         add_income_form = AddIncome()      
        
#     context = {'add_income_form': add_income_form}
    
#     return render(request, "dashboard/profile.html", context)

class Profile(View):
    template_name = 'dashboard/profile.html'
    add_income_form = AddIncome
    context = {
        "title": "Submit Url",
        "add_income_form": add_income_form,
        "pls_work": "pls work",
        "current_name": "",
        "user_name ": "",
        "c_id" : "",
        "income_name" : "",
        "deposit" : "",
    }
    



    
    def get(self, request):
        current_name = request.user.username
        user_name = request.user
        c_id = request.user.id
        income_name = request.POST.get('income_name')
        deposit = request.POST.get('deposit')
        
        context = {"name": current_name, 'user_name': user_name, "c_id":c_id, 'income_name' : income_name, 'deposit' : deposit}
        # return render(request, 'dashboard/profile.html', self.context)
        return render(request, self.template_name, self.context)

    # -----

    
    def showUser(self, request):
        current_name = request.user.username
        user_name = request.user
        c_id = request.user.id
        
        context = {"name": current_name, 'user_name': user_name, "c_id":c_id}
        return render(request, self.template_name, context)

    
    def ugh(self, request): 
        
        add_income_form = AddIncome(request.POST)    
        if request.method == 'POST':
            add_income_form = AddIncome(request.POST)
            if add_income_form.is_valid():
                user_id = request.user.id
                new_income = Income(income_name = request.POST.get('income_name'), deposit = request.POST.get('deposit'), current_user_id = user_id)
                new_income.save()
                # return render(request, self.template_name, {'add_income_form': add_income_form, 'pls_work': 'pls work'})
                return redirect('/accounts/profile/')
                # return HttpResponse("Pls work")
            else:
                return HttpResponse("HAHAHAHHA")
                
        else:
            add_income_form = AddIncome()      
        
        # context = {'add_income_form': add_income_form}
        # context = {'PLS': 'PLS WORKKKKKKKKKKKKKKKKKKKKK'}
        # self.render_to_response({'add_income_form': add_income_form, 'pls_work': 'pls work'})
        
        return render(request, self.template_name, self.context)




    


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