from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import UpdateAPIView



from travel_app.api.serializers import EmployeeSerializer,BookTripSerializer,EmployeeViewSerializer
from travel_app.models import Employee,BookTrip

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_detail_employee_view(request):
    if request.method=="GET":
        data=Employee.objects.all()
        serializer =EmployeeViewSerializer(data,many=True)
        return Response(serializer.data)



@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_booking_details_view(request):
    if request.method=='GET':
        data=BookTrip.objects.all()
        serializer = BookTripSerializer(data,many=True)
        return Response(serializer.data)





@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))
def api_update_employee_view(request,pk):
    emp=Employee.objects.get(id=pk)
    if request.method=='PUT':
        data={}
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()

            data['success']='Updated!!'
            return Response(serializer.data)

        return Response(serializer.data)







@api_view(['DELETE',])
@permission_classes((permissions.AllowAny,))
def api_delete_employee(request,pk):
    emp=Employee.objects.get(id=pk)
    if request.method=='DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def api_create_employee_view(request):
    if request.method=='POST':
        data={}
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data['success']='Registered!!'
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def api_BookTravel_view(request,pk):
    dat_t = Employee.objects.get(id=pk)
    dat=BookTrip(driver=dat_t)
    if request.method=='POST':
        data={}
        serializer = BookTripSerializer(dat,data=request.data)
        if serializer.is_valid():
            serializer.save()

            data['success']='Cab Booked!!'
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
