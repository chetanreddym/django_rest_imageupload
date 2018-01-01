from rest_framework import viewsets, filters
from imageupload_rest.serializers import UploadedImageSerializer # import our serializer
from imageupload.models import UploadedImage # import our model

class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer