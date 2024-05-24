import os
from django.conf import settings

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

class ImageUploadView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        
        if serializer.is_valid():
            image, dir_name = serializer.validated_data.values()
            new_dir = os.path.join(settings.MEDIA_ROOT, 'images', dir_name)

            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            path = os.path.join(new_dir, image.name)

            with open(path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            return Response({"message":"Image uploaded successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
    dir_name = serializers.CharField()