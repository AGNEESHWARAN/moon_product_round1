
from rest_framework import serializers
from travel_app.models import Employee,BookTrip
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=['username','name','location']

class BookTripSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookTrip
        fields=['p_name','pickup_time','p_pickup','p_destination','p_phone']
class EmployeeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields='__all__'
