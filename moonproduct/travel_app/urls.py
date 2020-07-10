from django.urls import path,include
from travel_app import views
app_name='travel_app'


urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signUp,name='signUp'),
    path('book_travel/',views.bookTravel,name='book'),
    path('summery/',views.summery,name='summery'),
    path('apidisp/',views.apiDisp,name='apidisp'),
    path('emplist/',views.emplist,name='emplist'),
]
