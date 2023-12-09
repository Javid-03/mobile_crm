from django import forms
from mobile.models import Mobile


class MobileForm(forms.ModelForm):
    class Meta:
        model= Mobile
        fields="__all__"

        widgets={
            "brand":forms.TextInput(attrs={"class":"form-control w-50"}),
            "model":forms.TextInput(attrs={"class":"form-control w-50"}),
            "price":forms.NumberInput(attrs={"class":"form-control w-50"}),
            "year":forms.NumberInput(attrs={"class":"form-control w-50"}),
            "color":forms.TextInput(attrs={"class":"form-control w-50"}),
        }