from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Post
from research.models import Proposal
from report.models import Record

def index(request):
    context = {
        'posts': Post.objects.all(),
        'proposals': Proposal.objects.all(),
        'records': Record.objects.all(),
    }
    return render(request, 'homepage/index.html', context)