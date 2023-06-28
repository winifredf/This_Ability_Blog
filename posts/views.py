from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def register(request):
    return render(request, 'register.html')

def login(request):
    if  username = request.POST.get('username') && password = request.POST.get('password')
        return render(request, 'login.html')
    else: return ('User could not be authenticated. Please try again.')

def logout(request):
    logout(request)
    return render(request, 'index.html')

