import json

from rest_framework import status

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from saf.models import User, Publication

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from saf.serialieur import UserSerialize, AddPublicaionSerializeur, UserListSerialize, publicationListSerialize, UpdatepublicationSerialze, DeletePublicationserialize


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
        return HttpResponse(json.dumps(serialze.data))

@api_view(['GET'])  
def lis_publication(request):
        queryset = Publication.objects.all().filter()
        serialize = publicationListSerialize(queryset, many=True)
        return HttpResponse(json.dumps(serialize.data))
    
@api_view(['POST'])
def publcation_user(request):
    user = request.data['user']
    queryset = Publication.objects.filter(user = user)
    serialize = publicationListSerialize(queryset, many=True)
    return HttpResponse(json.dumps(serialize.data))
    
############ post ####################
@api_view(['POST'])
def addUser(request, *args, **kwards):
        data = request.data
        serializer = UserSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data), status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addPublication(request, *args, **kwards):
        data = request.data
        serializer = AddPublicaionSerializeur(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #####  login ########
@api_view(['POST'])
def login(request):
    user_name = request.data['user_name']
    password = request.data['password']
    status_login = False
    queryset = User.objects.all().filter(user_name = str(user_name)).filter(password = str(password))
    serialize = UserListSerialize(queryset, many=True)
    if queryset :                                                                                        
        status_login = True
        return HttpResponse(json.dumps({'status': status_login, 'user': serialize.data[0]}))
    return HttpResponse(json.dumps({'status': status_login, 'user': {}}))
    
  
############# put ################
@api_view(['PUT'])     
def UpdateUser(request):
    id = request.data['id']
    queryset = User.objects.get(id=id)
    serialize = UserSerialize(queryset, data = request.data)
    if serialize.is_valid():
         serialize.save()
         return HttpResponse(json.dumps(serialize.data))
    return HttpResponse(serialize.errors)

@api_view(['PUT'])     
def UpdatePublication(request):
    id = request.data['id']
    queryset = Publication.objects.get(id=id)
    serialize = UpdatepublicationSerialze(queryset, data = request.data)
    if serialize.is_valid(): 
        serialize.save()
        return HttpResponse(json.dumps(serialize.data))
    return HttpResponse(serialize.errors, status=400)

         ##### DELETE PUBLICATION  ##################
@api_view(['PUT'])     
def deletePublication(request):
    id = request.data['id']
    queryset = Publication.objects.filter(id=id).update(status='true')
    print(queryset)
    serialize = DeletePublicationserialize(queryset, many=True)
    if serialize.is_valid():
        serialize.save()
    return HttpResponse(json.dumps({'publication': 'deleted'}))   
    


 ###########  delete ################

@api_view(['DELETE'])
def delete_user(request):
    id = request.data['id']
    queryset = User.objects.filter(id=id).delete()
    return HttpResponse(json.dumps(queryset))


    
 