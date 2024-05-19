from rest_framework import generics

from .models import Topics
from .serializers import TopicsSerializer

class ListCreateTopics(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer

class TopicUpdateAPIView(generics.UpdateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer