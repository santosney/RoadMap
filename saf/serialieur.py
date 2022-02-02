# from django.contrib.auth.models import User, Group
from dataclasses import field
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
    username = serializers.SerializerMethodField()
  
    class Meta:
        model = Publication
        fields = ['data', 'date_publication',  'status', 'user_id', 'id', 'user','username']
        
    def get_username(self,obj):
        return obj.user.user_name

# class  publicationSerialize(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Publication
       
#         fields = ['data', 'date_publication',  'status', 'user_id']
        
class AddPublicaionSerializeur(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['data', 'date_publication', 'status', 'user']