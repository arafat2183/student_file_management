from django.shortcuts import render


# Create your views here.
def about(request):
    context = {
        'active_page': 'about',
    }
    return render(request, 'about.html', context)
