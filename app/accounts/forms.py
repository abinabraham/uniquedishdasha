import datetime
import string

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email




class UserAuthenticationForm(AuthenticationForm):
    """
    Extends the standard django AuthenticationForm, to support 75 character
    usernames.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:            
            if field in self.errors:
                self.fields[field].widget.attrs['class']='form-control'