from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Student
#         fields=['id','name','roll','city']
# class StudentSerializer(serializers.ModelSerializer):
#     # name=serializers.CharField(read_only=True)

#     class Meta:
#         model=Student
#         fields=['id','name','roll','city']
#         read_only_fields=['name','roll']
# def starts_with_s(value):
#     if value[0].lower()!='s':
#         raise serializers.ValidationError('name should start with s')

class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model=Student
        fields=['id','name','roll','city']

    
    
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat full')
        return value
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='shivam' and ct.lower()!='ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data  
    
   
