from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from dashboard import incomeform
from dashboard.models import Users, Income, Bills
from dashboard import loginform
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from dashboard.loginform import UserForm
from dashboard.incomeform import AddIncome
from dashboard.billsform import AddBill
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
    
# def profile(request):
#     return render(request, 'dashboard/profile.html', {"hello": 'hello'})

# ----------
class IncomeProfile(View):
    template_name = 'dashboard/profile.html'
    add_income_form = AddIncome
    context = {
        "title": "Submit Url",
        "add_income_form": add_income_form,
        "pls_work": "pls work",
        "current_name": "",
        "user_name ": "",
        "c_id" : "",
        "income_names" : "",
        "deposit" : 0,
        "range": range(3),
        "user_income": ""
    }
    

    def get(self, request):
        # self.context['current_name'] = request.user.username
        user_name = request.user
        
        user_name = request.user.first_name
        c_id = request.user.id
        
        income_names = list(Income.objects.values_list('income_name', flat=True))[-3:]
        deposits = list(Income.objects.values_list('deposit', flat=True))[-3:]
        user_income = zip(income_names, deposits)
        
        self.context["c_id"] = c_id
        self.context["user_name"] = user_name
        self.context["income_names"] = income_names[-3:]
        self.context["deposits"] = deposits[-3:]
        self.context["pls_work"] = "LALSLSLLSLSLSLS"
        self.context["user_income"] = user_income
        

        return render(request, self.template_name, self.context)

    
    def post(self, request): 
        if request.method == 'POST':
            add_income_form = AddIncome(request.POST)
            self.context["add_income_form"] = add_income_form
            if add_income_form.is_valid():
                user_id = request.user.id
                new_income = Income(income_name = request.POST.get('income_name'), deposit = request.POST.get('deposit'), current_user_id = user_id)
                new_income.save()
                return redirect('/accounts/profile/')
        else:
            add_income_form = AddIncome()      

        return render(request, self.template_name, self.context['add_income_form'])



# -------------

class BillsProfile(View):
    template_name = 'dashboard/profile.html'
    bill_form = AddIncome
    context = {
        "title": "Submit Url",
        "bill_form": bill_form,
        "bill_name": "bill_name",
        "category": "category",
        "amount_due": 0,
        "isPaid ": False,
        "due_date": "",
        "pay_date": "",
        "bill_zip": ""
    }
    

    def get(self, request):
        
        bill_names = list(Bills.objects.values_list('bill_name', flat=True))[-3:]
        categories = list(Bills.objects.values_list('category', flat=True))[-3:]
        amounts_due = list(Bills.objects.values_list('amount_due', flat=True))[-3:]
        isPaids = list(Bills.objects.values_list('isPaid', flat=True))[-3:]
        
        bill_zip = zip(bill_names, categories, amounts_due, isPaids)
        
        self.context["bill_name"] = bill_names[-3:]
        self.context["categories"] = categories[-3:]
        self.context["amounts_due"] = amounts_due[-3:]
        self.context["isPaids"] = isPaids[-3:]

        self.context["bill_zip"] = bill_zip
        

        return render(request, self.template_name, self.context)

    
    def post(self, request): 
        if request.method == 'POST':
            bill_form = AddBill(request.POST)
            self.context["bill_form"] = bill_form
            if bill_form.is_valid():
                user_id = request.user.id
                new_bill = Bills(category = request.POST.get('category'), bill_name = request.POST.get('bill_name'), amount_due = request.POST.get('amount_due'), isPaid = request.POST.get('isPaid'), pay_date = request.POST.get('pay_date'), due_date = request.POST.get('due_date'), current_user_id = user_id)
                new_bill.save()
                return redirect('/accounts/profile/')
        else:
            bill_form = AddBill()      

        return render(request, self.template_name, self.context['bill_form'])
