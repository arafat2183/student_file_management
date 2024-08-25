from django.shortcuts import render


# Create your views here.
def blog(request):
    context = {
        'active_page': 'blog',
    }
    return render(request, 'blog.html', context)
