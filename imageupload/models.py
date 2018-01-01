from django.db import models
import uuid

# Our main model:Uploaded Image

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class UploadedImage(models.Model):
    image = models.ImageField("uploaded image", upload_to=scramble_uploaded_filename)
