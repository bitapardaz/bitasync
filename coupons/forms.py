from django import forms


class AddGiftCardForm(forms.Form): 
    hashcode = forms.CharField(max_length=500, required=True)
        
    
