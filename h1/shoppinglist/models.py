from django.db import models

class Item(models.Model):
   name = models.CharField(max_length=300)

   created = models.DateTimeField(auto_now_add=True, null=True)
   modified = models.DateTimeField(auto_now=True, null=True)

   plan = models.TextField(blank=True)

   done = models.BooleanField(default=False)

   def __str__(self):
       return self.name
