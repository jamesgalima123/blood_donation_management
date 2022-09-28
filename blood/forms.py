from django import forms

from . import models

class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        models=models.Announcement
        fields=['title','body']
class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit']
