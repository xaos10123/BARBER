from django import forms

from main.models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            "master": forms.Select(attrs={"class": "form-control"}),
            "services": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
