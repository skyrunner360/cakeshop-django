from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'home/home.html')

def contact(request):
    pass
def about(request):
    pass
def search(request):
    pass
def handleSignup(request):
    pass
def handleLogin(request):
    pass
def handleLogout(request):
    pass