from django.shortcuts import render


def login(request):
    context = {
        'title': 'login',
    }
    return render(request, 'login_index.html', context)


def register(request):
    context = {
        'title': 'register',
    }
    return render(request, 'register.html', context)
