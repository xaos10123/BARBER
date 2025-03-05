from django import forms

from main.models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            "master": forms.Select(attrs={"class": "form-select text-center"}),
            "services": forms.SelectMultiple(attrs={"class": "form-select text-center" , "style": "margin-top: 10px;"})
        }
