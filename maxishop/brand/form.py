from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        # to use all field from the model
        fields= "__all__"
