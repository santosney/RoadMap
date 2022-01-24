# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from saf.models import User, Publication


class UserSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_name', 'password']

class  publicationSerialize(serializers.HyperlinkedModelSerializer):
    user = UserSerialize()
    class Meta:
        model = Publication
       
        fields = ['data', 'date_publication',  'status', 'user']