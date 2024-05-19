from rest_framework import generics

from .models import Results, Goalscorers, Shootouts
from .serializers import ResultsSerializer, GoalscorersSerializer, ShootoutsSerializer

class ListCreateResults(generics.ListCreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

class ListCreateGoalscorers(generics.ListCreateAPIView):
    queryset = Goalscorers.objects.all()
    serializer_class = GoalscorersSerializer

class ListCreateShootouts(generics.ListCreateAPIView):
    queryset = Shootouts.objects.all()
    serializer_class = ShootoutsSerializer