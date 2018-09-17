from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'contact/post_list.html', {})
