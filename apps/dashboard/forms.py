from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.news.models import Article, Category


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password check", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title", "class": "form-control"}))
    summary = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Summary", "class": "form-control"}))
    content = forms.CharField(widget=CKEditorWidget())
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"})
    )
    published_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
                "data-toggle": "datetimepicker",
            }
        ),
    )
    is_published = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'category', 'published_date', 'is_published']
