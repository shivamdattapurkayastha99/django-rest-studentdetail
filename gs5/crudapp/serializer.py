from rest_framework import serializers
from .models import Student
def starts_with_s(value):
    if value[0].lower()!='s':
        raise serializers.ValidationError('name should start with s')

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[starts_with_s])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
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
    
