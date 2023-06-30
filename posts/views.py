from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request,'signup.html')
#def login(request):
    if  "username" == request.POST.get('username') and "password" == request.POST.get('password'):
        return render(request, 'login.html')
    else: return ('User could not be authenticated. Please try again.')

#def logout(request):
    logout(request)
    return render(request, 'index.html')

#def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'login.html')
    else:
        return render(request,'signup.html')

