from typing import Any, Dict

from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from apps.accounts.models import Author
from apps.core.utils import GetObjectMixin
from apps.dashboard.forms import ArticleForm, LoginForm, SignUpForm
from apps.news.models import Article, Category


def get_statistics() -> dict[str, Any] | None:
    data = {'total_published': Article.objects.filter(is_published=True).count()}
    data['total_pending'] = Article.objects.filter(is_published=False).count()
    data['total_authors'] = Author.objects.count()
    data['total_categories'] = Category.objects.count()
    return data


class ArticleListView(ListView):
    model = Article
    template_name = 'home/index.html'
    context_object_name = 'articles'
    ordering = ['-published_date']
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(get_statistics())
        return context


class ArticleCreateUpdateView(GetObjectMixin, CreateView, UpdateView):
    model = Article
    template_name = 'home/create-update-article.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    success_url = reverse_lazy('articles_list')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = None
        article_id = kwargs.get("article_id")
        if article_id:
            self.object = self.get_object_by_model(Article, article_id)
            self.template_name = 'home/update-article.html'
        else:
            self.template_name = 'home/create-article.html'
        return super().get(request, *args, **kwargs)

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user.author
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(get_statistics())
        return context


def login_view(request: HttpRequest) -> HttpResponse:
    print('got here')
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request: HttpRequest) -> HttpResponse:
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
