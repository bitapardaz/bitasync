from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.Form): 
    # additional general information regarding a customer.
    # We use this form the the registration stage. 

    email = forms.EmailField(max_length=100)
    mobile = forms.CharField(max_length=20, required=False)
    is_shop = forms.BooleanField(required=False)    
    #email_subscription = forms.BooleanField(required=False)

    address = forms.CharField(max_length=100, required=False)
    landline = forms.CharField(max_length=20, required=False)  
    read_agreement = forms.BooleanField(required=True)
    
    def clean_email(self):

        email = self.cleaned_data["email"]
        users_with_existing_email = User.objects.filter(email=email)
        
        if users_with_existing_email: 
            raise forms.ValidationError('duplicate_email', code='duplicate_email')                
        else: 
            return email            


    
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
        

#    def clean_email(self):
        # we should make sure that there is only one user with this email.
        
#        email = self.cleaned_data['email']
        
#        if "email" in self.changed_data: 
        
#            users_with_existing_email = User.objects.filter(email=email)
            
#            if users_with_existing_email: 
#                raise forms.ValidationError('duplicate_email', code='duplicate_email') 
#            else: 
#                return email               
        
#        else: 
#            return email
               

