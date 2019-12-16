from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# rest_framework imports
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from doctorslist.models import Doctors
from doctorslist.serializers import DoctorsSerializer

class DoctorsView(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    @action(methods=['GET'], detail=False, url_path="find_doctors")
    def find_doctors(self, request):
    	file=open("C://Users//snehil//Desktop//Tests.txt","r")
    	a=file.readline()
    	find_doctors = Doctors.objects.filter(locality=a)
    	serializer = DoctorsSerializer(find_doctors, many=True)
    	return Response(serializer.data, status.HTTP_200_OK)
    	
    @action(methods=['GET'], detail=False, url_path="find_specialization")
    def post_doctors(self, request):
    	file=open("C://Users//snehil//Desktop//Tests.txt","r")
    	a=file.readline()
    	find_spec = Doctors.objects.filter(category__icontains=a)
    	serializer = DoctorsSerializer(find_spec, many=True)
    	return Response(serializer.data, status.HTTP_200_OK)
    

