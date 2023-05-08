from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the travel index.")

def profile_view(request):
    return render(request, 'users/profile.html')