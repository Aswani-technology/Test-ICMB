from django.urls import URLPattern, path
from .views import *
urlpatterns=[
    path('home/',home),
    path('insert/',sales_insert),
    path('list/',sales_list),
    path('formdisplay',form_display,name="formdisplay") # Ajax request to display data in a form
 
]
