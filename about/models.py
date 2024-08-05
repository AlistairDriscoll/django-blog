from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    Renders the most recent about post made by the website author
    and recieves collaboration requests
    Displayes an individual instance of :model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``Collaberate form``
        an instance of :form:`about.CollaborateForm`
    :template:`about/about.html`
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"