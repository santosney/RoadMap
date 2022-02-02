from rest_framework import status

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from saf.models import User, Publication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from saf.serialieur import UserSerialize, AddPublicaionSerializeur, UserListSerialize, publicationListSerialize


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializeur_class = UserSerialize
    # permission_class = [permissions.IsAuthenticated]
    
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    # serializeur_class = publicationSerialize
    # permission_class = permissions[permissions.IsAuthenticated]
    
############# get ################
@api_view(['GET'])  
def listuser(request):
        queryset = User.objects.all()
        serialze = UserListSerialize(queryset, many=True)
        return JsonResponse(serialze.data, safe=False)

@api_view(['GET'])  
def lis_publication(request):
        queryset = Publication.objects.all()
        serialize = publicationListSerialize(queryset, many=True)
        return JsonResponse(serialize.data, safe=False)

############ post ####################
@api_view(['POST'])
def addUser(request, *args, **kwards):
        data = request.data
        serializer = UserSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addPublication(request, *args, **kwards):
        data = request.data
        serializer = AddPublicaionSerializeur(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    user_name = request.data['user_name']
    password = request.data['password']
    status_login = False
    if User.objects.all().filter(user_name = str(user_name)).filter(password = str(password)):
        status_login = True
        return HttpResponse(status_login)
    return HttpResponse(status_login)
  
    
    
############# put ################
@api_view(['PUT'])     
def UpdateUser(request, id):
     queryset = User.objects.get(id=id)
     serialize = UserSerialize(queryset, data = request.data)
     if serialize.is_valid():
         serialize.save()
         return JsonResponse(serialize.data)
     return JsonResponse(serialize.errors, status=400)

@api_view(['PUT'])     
def UpdatePublication(request, id):
     queryset = User.objects.get(id=id)
     serialize = publicationSerialize(queryset, data = request.data)
     if serialize.is_valid():
         serialize.save()
         return JsonResponse(serialize.data)
     return JsonResponse(serialize.errors, status=400)
 
 ###########  delete ################

@api_view(['DELETE'])
def delete_user(request, id):
    queryset = User.objects.get(id = id)
    serialize = UserSerialize(queryset)
    serialize.delete()
    return HttpResponse('user deleted !')


    
 