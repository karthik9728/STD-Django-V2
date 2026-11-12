from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # to use all field from the model
        # fields= "__all__"
        fields= ["name"]

    def clean_name(self):
        name = self.cleaned_data.get('name')

        # Minimum length
        if len(name.strip()) < 2 :
            raise forms.ValidationError("Category name must contain at least 2 characters.")

        # Maximum length
        if len(name.strip()) > 50:
            raise forms.ValidationError("Category name cannot exceed 50 characters.")

        # Duplicate validation
        if Category.objects.filter(name__iexact=name.strip()).exists():
            raise forms.ValidationError("This category already exists.")

        return name.strip()

