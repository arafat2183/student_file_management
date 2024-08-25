from django.shortcuts import render


# Create your views here.
def services(request):
    context = {
        'active_page': 'services',
    }
    return render(request, 'services.html', context)
