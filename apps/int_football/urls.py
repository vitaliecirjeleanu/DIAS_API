from django.urls import path

from . import views

urlpatterns = [
    path('goalscorers',views.ListCreateGoalscorers.as_view(), name='int_football-goalscorers'),
    path('results',views.ListCreateResults.as_view(), name='int_football-results'),
    path('shootouts',views.ListCreateShootouts.as_view(), name='int_football-shootouts'),
]