import json
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from .serializer import UserSerializer,propertyInfoSerializer,clientInfoSerializer,PropertySerializer,reviewSerializer
from .models import User,clientInfo,propertyInfo,PropertyReview
from rest_framework.exceptions import PermissionDenied



# Create your views here.



class CreateUser(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        data = self.get_serializer(data=request.data)
        if data.is_valid():
            new_data = data.validated_data
            user = User.objects.create_user(**new_data)
            refresh = RefreshToken.for_user(user)
            print(user)
            data = {
                "username": user.username,
                "email": user.email,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                
            }
            print(data)
            return Response({"data": data}, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class clientInfo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = clientInfoSerializer

    def get_queryset(self):
        return clientInfo.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        data=request.data
        data['user']=request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class propertyInformation(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_queryset(self):
        # Allow access only if the user is a superuser
        if not self.request.user.is_superuser:
            raise PermissionDenied("Only superusers can access this resource.")
        return propertyInfo.objects.all()

    def get(self, request):
        
        property_id = request.query_params.get('id', None)  # Use `query_params` for query params in URL
        if property_id:
            try:
                property = propertyInfo.objects.get(id=property_id)
                serializer = self.get_serializer(property)
                return Response(serializer.data)
            except :
                return Response({"error": "Property not found"}, status=404)
        else:
            properties= propertyInfo.objects.prefetch_related('images_read').all()
            serializer = propertyInfoSerializer(properties, many=True)
            return Response(serializer.data)
           
    def post(self, request, *args, **kwargs):
        # Handle POST requests to create a new clientInfo object
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can create client info.")
        data = request.data
        serializer = self.get_serializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Handle DELETE requests to delete a specific clientInfo object by ID
        id=request.query_params.get('id',None)
        if not id:
           return Response({'Error':'Enter Item Id'},status=status.HTTP_400_BAD_REQUEST)
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can delete client info.")
        
          # Expecting the client ID in the request data
        try:
            property = propertyInfo.objects.get(id=id)
            property.delete()
            return Response({"message": "Client info deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except clientInfo.DoesNotExist:
            return Response({"error": "Client info not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def path(self,request,*args,**kwargs):
        id=request.query_params.get('id',None)
        if id:
            try:
                property = propertyInfo.objects.get(id=id)

            except :
                return Response({"error": "Property not found"}, status=404)
        else:
            return Response({'Error':'specify property with id'},status=status.HTTP_400_BAD_REQUEST)
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can create client info.")
        data = request.data
        serializer = self.get_serializer(property,data=data,partial=True)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class onLoad(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PropertySerializer

    def get_queryset(self):
        return propertyInfo.objects.prefetch_related('images_read').all()

    def get(self, request):
        try:
            id=request.query_params.get('id',None)
            if not id:
                 serializer = self.get_serializer(self.get_queryset(),many=True)
                 return Response(serializer.data)
            property =propertyInfo.objects.prefetch_related('images_read').get(id=id)
            serializer=self.get_serializer(property)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"error":'An error Occured'}, status=status.HTTP_400_BAD_REQUEST)



