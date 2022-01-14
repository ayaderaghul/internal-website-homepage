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
from .models import Record


def home(request):
    context = {
        'records': Record.objects.all()
    }
    return render(request, 'report/home.html', context)


class RecordListView(ListView):
    model = Record
    template_name = 'report/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'records'
    ordering = ['-date_posted']
    paginate_by = 5


class UserRecordListView(ListView):
    model = Record
    template_name = 'report/user_records.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'records'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Record.objects.filter(author=user).order_by('-date_posted')


class RecordDetailView(DetailView):
    model = Record

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['niches', 'project', 'token', 'ecosystem', 'launch',
    'category', 'website', 'twitter', 'overview', 'comment',
    'rate', 'content', 'date_posted', 'author', 'keywords']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Record
    fields = ['niches', 'project', 'token', 'ecosystem', 'launch',
    'category', 'website', 'twitter', 'overview', 'comment',
    'rate', 'content', 'date_posted', 'author', 'keywords']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        record = self.get_object()
        if self.request.user == record.author:
            return True
        return False


class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Record
    success_url = '/'

    def test_func(self):
        record = self.get_object()
        if self.request.user == record.author:
            return True
        return False
