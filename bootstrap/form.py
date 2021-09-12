from django import forms
from .models import formModel

class RegForm(forms.ModelForm):
    class Meta:
        model = formModel
        fields = ["email", "phone",]
        labels = {"email": "Email Address", "phone": "Phone Number",}