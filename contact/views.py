from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import MyModelForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    #Post.objects.get(pk=pk)
    posts = Post.objects.order_by('First_Name')
    return render(request, 'contact/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'contact/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MyModelForm()
    return render(request, 'contact/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = MyModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MyModelForm(instance=post)
    return render(request, 'contact/post_edit.html', {'form': form})

