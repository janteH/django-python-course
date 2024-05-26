from django.urls import path
from .views import *

urlpatterns = [
		path('about', AboutView.as_view()),
		path('', ListView.as_view()),
		path('item/new', CreateView.as_view()),
		path('item/<int:pk>/delete', DeleteView.as_view()),
		path('item/<int:pk>', UpdateView.as_view()),
]
