from django.shortcuts import render


# Create your views here.
def contact(request):
    context = {
        'active_page': 'contact',
    }
    return render(request, 'contact.html', context)
