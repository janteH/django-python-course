from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class AboutView(TemplateView):
		template_name = "shoppinglist/about.html"
		
class ListView(ListView):
        model = Item
        
class UpdateView(UpdateView):
        model = Item
        fields = ["name"]
        success_url = "/"
     
class CreateView(CreateView):
        model = Item
        fields = ["name"]
        success_url = "/"
        
class DeleteView(DeleteView):
        model = Item
        success_url = "/"
