from django import forms
from .models import SalesTeam
class FormContactForm(forms.ModelForm):
    class Meta:
        model= SalesTeam
        fields= ["firstname","lastname","email", "phone", "company","hear_about_us","comment"]