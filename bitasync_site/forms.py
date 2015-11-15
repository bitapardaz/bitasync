from django import forms

class Contact_us(forms.Form): 
    
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    

    
