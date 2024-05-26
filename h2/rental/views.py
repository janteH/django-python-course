from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import *

class RentalView(TemplateView):
	template_name = "rental/rental.html"

class ItemListView(ListView):
	model = Item

class PersonListView(ListView):
	model = Person

class ItemCreateView(CreateView):
	model = Item
	fields = ["name", "person"]
	success_url = "/"
	
class PersonCreateView(CreateView):
	model = Person
	fields = ["name"]
	success_url = "/"

class ItemUpdateView(UpdateView):
	model = Item
	fields = ["name", "person", "description"]
	success_url = "/"

class PersonUpdateView(UpdateView):
	model = Person
	fields = ["name", "info"]
	success_url = "/"

class ItemDeleteView(DeleteView):
	model = Item
	success_url = "/"

class PersonDeleteView(DeleteView):
	model = Person
	success_url = "/"
