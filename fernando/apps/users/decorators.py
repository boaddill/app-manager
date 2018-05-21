from django.core.exceptions import PermissionDenied
from .models import User ,Profile_Client

def superuser(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap



def is_client(function):
    def wrap(request ,*args, **kwargs):
        try:
            client_profile = Profile_Client.objects.get(id=kwargs['id'])
            if client_profile.user.id == request.user.id or request.user.is_superuser:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied

        except :
            pass
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_employee(function):
    def wrap(request ,*args, **kwargs):
        try:
            employee_profile = Profile_Employee.objects.get(id=kwargs['id_user'])
            if request.user.is_employee or request.user.is_superuser:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except:
            pass
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap