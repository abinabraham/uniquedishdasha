
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( IndexView,DummyView, origin_airport_search, \
                    ProfileView, ProfileViewGet, PendingOrdersView,\
                    generatePdf, generatePrint, GalleryView)

app_name = 'dashboard'

# URLs dashboard
urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('origin_airport_search/', origin_airport_search, name='origin_airport_search'),
    path('profile/', login_required(ProfileView.as_view()), name='customer_profile'),
    path('profile/<str:id>', login_required(ProfileViewGet.as_view()), name='customer_profile_get'),

    path('pending/orders/', login_required(PendingOrdersView.as_view()), name='pending_ordrs'),
    path('pdf/<str:cid>/<str:value>', generatePdf, name='invoice_pdf'),
    path('print/<str:cid>/', generatePrint, name='print_generate'),
    path('gallery/', login_required(GalleryView.as_view()), name='gallery'),



]