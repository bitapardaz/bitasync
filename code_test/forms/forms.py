from django import forms


class KidForm(forms.Form):
    name = forms.CharField(max_length=20, label="name")
    address = forms.CharField(max_length=100, label="address")


class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField(widget=forms.Textarea)
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)
