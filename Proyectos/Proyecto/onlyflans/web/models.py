import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    ingredients = models.TextField()  # Campo para los ingredientes
    ingredients_description = models.TextField() 
    preparation = models.TextField()  # Campo para la preparación
    preparation_description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_email} - Mensaje: {self.message}"
