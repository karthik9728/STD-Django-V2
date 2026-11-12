from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        # to use all field from the model
        # fields= "__all__"
        fields= ["name"]

    def clean_name(self):
        name = self.cleaned_data.get('name')

        # Minimum length
        if len(name.strip()) < 2 :
            raise forms.ValidationError("Brand name must contain at least 2 characters.")

        # Maximum length
        if len(name.strip()) > 50:
            raise forms.ValidationError("Brand name cannot exceed 50 characters.")

        # Duplicate validation
        if Brand.objects.filter(name__iexact=name.strip()).exists():
            raise forms.ValidationError("This brand already exists.")

        return name.strip()

