from django.urls import path,include

from travel_app.api.views import api_detail_employee_view,api_booking_details_view,api_update_employee_view,api_delete_employee,api_create_employee_view,api_BookTravel_view

urlpatterns=[
    path('employee/',api_detail_employee_view,name='emp_details'),
    path('bookings/',api_booking_details_view,name='bookings'),
    path('update/<int:pk>',api_update_employee_view,name='update'),
    path('delete/<int:pk>',api_delete_employee,name='delete'),
    path('create/',api_create_employee_view,name='create'),
    path('book_trip/<int:pk>',api_BookTravel_view,name='book'),
]
