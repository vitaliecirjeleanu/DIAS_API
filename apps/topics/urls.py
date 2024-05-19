from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateTopics.as_view(), name='topics'),
    path('<int:pk>/update', views.TopicUpdateAPIView.as_view(), name='topic-update'),
]