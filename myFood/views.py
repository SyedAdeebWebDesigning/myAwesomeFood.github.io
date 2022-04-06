from django.shortcuts import redirect, render
from .forms import UserCreationForm, SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def food(request):
    return render(request, 'food.html')


def account(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'account.html', {'form': form})


def contact(request):
    from .models import Contact
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        
        return redirect('thanks')
    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')

def register(request):
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data('username')
        password = form.cleaned_data('password1')
        form.save()
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('index')

    
    form = SignUpForm()
    context = {'form': form}

    return render(request, 'register.html', context)
