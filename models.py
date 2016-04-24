"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Monday, January 4, 2016
"""

# Imports
from django.db import models
from django.contrib.auth.models import User

"""
KitState
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > States
"""
class KitState( models.Model ) :
    
    description = models.TextField( max_length = None, default = '' )
    value = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.description
    # End of unicode function
    
# End of Kit State model

"""
RegisterState
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > States
"""
class RegisterState( models.Model ) :
    
    description = models.TextField( max_length = None, default = '' )
    value = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.description
    # End of unicode function
    
# End of RegisterState class