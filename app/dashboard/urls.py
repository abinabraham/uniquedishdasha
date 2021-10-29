
from django.urls import path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( IndexView, origin_airport_search)

app_name = 'dashboard'

# URLs dashboard
urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('origin_airport_search/', origin_airport_search, name='origin_airport_search')
]