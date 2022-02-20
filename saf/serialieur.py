# from django.contrib.auth.models import User, Group

from rest_framework import serializers
from saf.models import User, Publication

########### User #####################

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_name', 'password']
        
class UserListSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_name', 'id']

######### Publication #################
class  publicationListSerialize(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
  
    class Meta:
        model = Publication
        fields = ['data', 'date_publication',  'status', 'id', 'user','user_name']
        
    def get_user_name(self,obj):
        return obj.user.user_name

        
class AddPublicaionSerializeur(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['data', 'date_publication', 'status', 'user', 'id']
        
class UpdatepublicationSerialze(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'user', 'data']
        
class DeletePublicationserialize(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['data', 'date_publication', 'status', 'user', 'id']