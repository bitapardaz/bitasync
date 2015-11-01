from django import forms


class KidForm(forms.Form):
    name = forms.CharField(max_length=20, label="نام")
    address = forms.CharField(max_length=100, label="address")
