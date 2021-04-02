from django import forms
from .models import Post, Category

# query from db category with for loop ( must import Category )
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
      choice_list.append(item)
# end query

class PostForm(forms.ModelForm):
      class Meta:
            model = Post
            fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'headers_image')

            widgets = {
                  'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title', 'autocomplete': 'off'}),
                  'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                  'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'userId', 'readonly': True}),
                  #'author': forms.Select(attrs={'class': 'form-control'}),
                  'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
                  'body': forms.Textarea(attrs={'class': 'form-control'}),
                  'snippet': forms.Textarea(attrs={'class': 'form-control', 'value': 'Read more'}),
            }

class EditPostForm(forms.ModelForm):
      class Meta:
            model = Post
            fields = ('title', 'title_tag', 'category', 'body', 'snippet')

            widgets = {
                  'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title', 'autocomplete': 'off'}),
                  'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                  # 'author': forms.Select(attrs={'class': 'form-control'}),
                  'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
                  'body': forms.Textarea(attrs={'class': 'form-control'}),
                  'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            }