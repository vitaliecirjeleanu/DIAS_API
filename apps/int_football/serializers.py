from rest_framework import serializers

from .models import Results, Goalscorers, Shootouts

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Results
        fields = '__all__'

class GoalscorersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goalscorers
        fields = '__all__'

class ShootoutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shootouts
        fields = '__all__'