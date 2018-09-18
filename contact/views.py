from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('First_Name')
    return render(request, 'contact/post_list.html',{'posts': posts})

