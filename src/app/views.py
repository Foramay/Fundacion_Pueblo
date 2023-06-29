from django.shortcuts import render

def home(request):
    template_name = 'home.html'
    return render(request, template_name, {})


def login(request):
    template_name = 'login.html'
    return render(request, template_name, {})
