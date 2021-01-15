from rest_framework.serializers import ModelSerializer
from .models import Singer,Song
class SongSerializer(ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']
class SingerSerializer(ModelSerializer):
    sungby=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','sungby']