from django.urls import path
from .views import *

urlpatterns = [
	path('', RentalView.as_view()),
	path('list', ItemListView.as_view()),
	path('person', PersonListView.as_view()),
	path('item/new', ItemCreateView.as_view()),
	path('person/new', PersonCreateView.as_view()),
	path('item/<int:pk>', ItemUpdateView.as_view()),
	path('person/<int:pk>', PersonUpdateView.as_view()),
	path('item/<int:pk>/delete', ItemDeleteView.as_view()),
	path('person/<int:pk>/delete', PersonDeleteView.as_view()),
]
