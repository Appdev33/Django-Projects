
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.stockPicker,name='stockepicker'),
    path('stocktracker/',views.stockTracker,name='stocketraccker'),
]