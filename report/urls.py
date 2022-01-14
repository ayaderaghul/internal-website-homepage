from django.urls import path
from .views import (
    RecordListView,
    RecordDetailView,
    RecordCreateView,
    RecordUpdateView,
    RecordDeleteView,
    UserRecordListView
)
from . import views

urlpatterns = [
    path('', RecordListView.as_view(), name='report-home'),
    path('user/<str:username>', UserRecordListView.as_view(), name='user-records'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record-detail'),
    path('record/new/', RecordCreateView.as_view(), name='record-create'),
    path('record/<int:pk>/update/', RecordUpdateView.as_view(), name='record-update'),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record-delete'),
]
