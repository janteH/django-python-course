from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField(blank=True)
	person = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=150)
	info = models.TextField(blank=True)

	def __str__(self):
		return self.name
