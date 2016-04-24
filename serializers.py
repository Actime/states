# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from rest_framework import serializers
from .models import KitState, RegisterState

"""
KitState Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > States
"""
class KitStateSerializer( serializers.ModelSerializer ) :

    """
    Meta class for serializer information
    """
    class Meta :
        model = KitState
        fields = (
            'id',
            'description',
            'value',    
        )
    # End of Meta class
    
# End of KitState Serializer class

"""
RegisterState Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > States
"""
class RegisterStateSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = RegisterState
        fields = (
            'id',
            'description',
            'value',      
        )
    # End of Meta class
    
# End of RegisterState Serializer class