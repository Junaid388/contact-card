from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    #Post.objects.get(pk=pk)
    posts = Post.objects.order_by('First_Name')
    return render(request, 'contact/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'contact/post_detail.html', {'post': post})

