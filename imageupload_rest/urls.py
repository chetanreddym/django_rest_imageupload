from django.conf.urls import url, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadedImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadedImageViewSet, 'images')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
