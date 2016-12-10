# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 5, 2016
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import KitState, RegisterState
from .serializers import KitStateSerializer, RegisterStateSerializer

"""
Kit State List Api View
Object list and creation
"""
class KitStateList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = KitState.objects.all()
    # Serializer class
    serializer_class = KitStateSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Kit State List class

"""
Kit State Detail Api View
"""
class KitStateDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = KitState.objects.all()
    # Serializer class
    serializer_class = KitStateSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Kit State Detail class

"""
Register State List Api View
Object list and creation
"""
class RegisterStateList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set variable
    queryset = RegisterState.objects.all()
    # Serializer class
    serializer_class = RegisterStateSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Register State List class

"""
Register State Detail Api View
"""
class RegisterStateDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = RegisterState.objects.all()
    # Serializer class
    serializer_class = RegisterStateSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Register State Detail class