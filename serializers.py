from rest_framework import serializers

from doctorslist.models import Doctors

class DoctorsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Doctors
		fields=['name','address','category','locality']