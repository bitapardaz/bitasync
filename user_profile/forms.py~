from django import forms
from .models import UserProfile


class UserProfileForm(forms.Form): 
    # additional information regarding a customer that we get 
    # at the point of registration. 

    email = forms.EmailField(max_length=100)
    mobile = forms.CharField(max_length=20, required=False)
    is_shop = forms.BooleanField(required=False)    
    #email_subscription = forms.BooleanField(required=False)

    address = forms.CharField(max_length=100, required=False)
    telephone = forms.CharField(max_length=20, required=False)  
    read_agreement = forms.BooleanField(required=True)
    
    
class MyProfileCustomerForm(forms.Form): 

    # do not show the username to the user. 
#    username = forms.CharField()
    email = forms.EmailField(max_length=100)
    mobile = forms.CharField(max_length=20, required=False)
    email_subscription = forms.BooleanField(required=False)
 
    
class MyProfileShopForm(forms.Form):
 
    email = forms.EmailField(max_length=100)
    mobile = forms.CharField(required=False)
    address = forms.CharField(max_length=100, required=False)
    landline = forms.CharField(max_length=20, required=False)  
    email_subscription = forms.BooleanField(required=False)
    
    # readonly field
    reward = forms.IntegerField(required=False) 
    bank_card_number = forms.CharField(max_length=100, required=False)
    account_holder = forms.CharField(max_length=100, required=False)
   
    def __init__(self,*args,**kwargs): 
        super(MyProfileShopForm,self).__init__(*args,**kwargs)
        self.fields['reward'].widget.attrs['readonly'] = True
        
        
