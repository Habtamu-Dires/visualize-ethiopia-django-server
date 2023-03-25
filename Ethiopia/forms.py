from django import forms
from .models import Element

#create your forms here.

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element        
        fields = ('title', 'description', 'source_name', 'source_url', 'file_type',)
        
