class MyModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['Category']
