from django.db import models
from django.db.models import aggregates
from django.utils import timezone
# Create your models here.

now = timezone.now()


class print_options(models.Model):
    print_name = models.CharField(max_length=200, verbose_name="printername")
    doc_file = models.CharField(max_length=300, verbose_name="docfile")
    copies = models.DecimalField(max_digits=3,decimal_places=0, verbose_name="copies")
    layout = models.CharField(max_length=300, verbose_name="layout")
    colored = models.CharField(max_length=300, verbose_name="colored")
    sizee = models.DecimalField(max_digits=3,decimal_places=0, verbose_name="sizee")
    pages = models.CharField(max_length=300, verbose_name="pages")
    
    

