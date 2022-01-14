from django.urls import path
from . import views


from .views import (
    KeywordListView,
    KeywordDetailView,
    KeywordCreateView,
    KeywordUpdateView,
    KeywordDeleteView,
    UserKeywordListView
)

urlpatterns = [
    path('', KeywordListView.as_view(), name='keyword-home'),
    path('user/<str:username>', UserKeywordListView.as_view(), name='user-keywords'),
    path('keyword/<int:pk>/', KeywordDetailView.as_view(), name='keyword-detail'),
    path('keyword/new/', KeywordCreateView.as_view(), name='keyword-create'),
    path('keyword/<int:pk>/update/', KeywordUpdateView.as_view(), name='keyword-update'),
    path('keyword/<int:pk>/delete/', KeywordDeleteView.as_view(), name='keyword-delete'),
]
