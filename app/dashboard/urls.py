
from django.urls import path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( IndexView,DummyView, origin_airport_search)

app_name = 'dashboard'

# URLs dashboard
urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('origin_airport_search/', origin_airport_search, name='origin_airport_search'),

    #Dummy
    path('dummy/1/', login_required(DummyView.as_view()), name='dummy'),

]