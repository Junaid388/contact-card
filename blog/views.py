from django.shortcuts import render

# Create your views here.


class CreateMyModelView(CreateView):
    model = Post
    form_class = MyModelForm
    template_name = 'myapp/template.html'
    success_url = 'myapp/success.html'
