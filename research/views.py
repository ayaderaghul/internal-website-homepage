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
from .models import Proposal


def home(request):
    context = {
        'proposals': Proposal.objects.all()
    }
    return render(request, 'research/home.html', context)


class ProposalListView(ListView):
    model = Proposal
    template_name = 'research/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'proposals'
    ordering = ['-date_posted']
    paginate_by = 5


class UserProposalListView(ListView):
    model = Proposal
    template_name = 'research/user_proposals.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'proposals'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Proposal.objects.filter(author=user).order_by('-date_posted')


class ProposalDetailView(DetailView):
    model = Proposal 

class ProposalCreateView(LoginRequiredMixin, CreateView):
    model = Proposal
    fields = ['title', 'business_model', 'hr_partner', 'finance',
        'technology', 'partner_user_ecosystem', 'community',
        'roadmap', 'competitor', 'marketcap', 'tokenomics',
        'fomo', 'content', 'date_posted', 'author', 'keywords']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProposalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Proposal
    fields = ['title', 'business_model', 'hr_partner', 'finance',
        'technology', 'partner_user_ecosystem', 'community',
        'roadmap', 'competitor', 'marketcap', 'tokenomics',
        'fomo', 'content', 'date_posted', 'author', 'keywords']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        proposal = self.get_object()
        if self.request.user == proposal.author:
            return True
        return False


class ProposalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Proposal
    success_url = '/'

    def test_func(self):
        proposal = self.get_object()
        if self.request.user == proposal.author:
            return True
        return False
