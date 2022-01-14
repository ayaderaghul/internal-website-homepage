from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Keyword


def home(request):
    context = {
        'keywords': Keyword.objects.all()
    }
    return render(request, 'topics/home.html', context)



class KeywordListView(ListView):
    model = Keyword
    template_name = 'topics/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'keywords'
    # ordering = ['-date_posted']
    paginate_by = 5


class UserKeywordListView(ListView):
    model = Keyword
    template_name = 'topics/user_keywords.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'keywords'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
 
        return Keyword.objects.filter(author=user)


class KeywordDetailView(DetailView):
    model = Keyword


class KeywordCreateView(LoginRequiredMixin, CreateView):
    model = Keyword
    fields = ['name', 'description', 'followedbys']

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

class KeywordUpdateView(LoginRequiredMixin, UpdateView):
    model = Keyword
    fields = ['name', 'description', 'followedbys']

    def form_valid(self, form):
        return super().form_valid(form)



class KeywordDeleteView(LoginRequiredMixin, DeleteView):
    model = Keyword
    success_url = '/'


