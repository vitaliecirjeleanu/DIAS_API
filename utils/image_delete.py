from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os

class ImageDeleteView(APIView):
    def delete(self, request):
            dir, name = request.data.values()
            file_path = os.path.join(settings.MEDIA_ROOT, 'images', dir, name)
            
            if os.path.exists(file_path):
                os.remove(file_path)
                return Response({"message": "Image deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

