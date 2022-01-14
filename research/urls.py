from django.urls import path
from .views import (
    ProposalListView,
    ProposalDetailView,
    ProposalCreateView,
    ProposalUpdateView,
    ProposalDeleteView,
    UserProposalListView
)
from . import views

urlpatterns = [
    path('', ProposalListView.as_view(), name='proposal-home'),
    path('user/<str:username>', UserProposalListView.as_view(), name='user-proposals'),
    path('proposal/<int:pk>/', ProposalDetailView.as_view(), name='proposal-detail'),
    path('proposal/new/', ProposalCreateView.as_view(), name='proposal-create'),
    path('proposal/<int:pk>/update/', ProposalUpdateView.as_view(), name='proposal-update'),
    path('proposal/<int:pk>/delete/', ProposalDeleteView.as_view(), name='proposal-delete'),
]
