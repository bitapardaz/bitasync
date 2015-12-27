from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class MyUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)  
    mobile = forms.CharField(max_length=20, required=False)
#    is_shop = forms.BooleanField(required=False)  
    
#    address = forms.CharField(max_length=100, required=False)
#    telephone = forms.CharField(max_length=20, required=False)  
#    read_agreement = forms.BooleanField(required=True)  
        
#    class Meta:
#        model = User
#        fields = ('username', 'password1', 'password2', 'email', 'mobile', 'is_shop', 'address', 'telephone', 'read_agreement' )
        
        
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email','mobile')
    
    def clean_email(self): 
        return "email" 

    def clean_mobile(self): 
        return "mobile"
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
        
class ShopForm(forms.Form):

    shop_id = forms.CharField()
    

CUSTOM_CHOICES = (('L1', 'L1'),
                  ('L2', 'L2'),
                  ('L5', 'L5'),
                  ('U1', 'U1'),
                  ('U3', 'U3'),
                  ('U6', 'U6'),
                 )
     
#class CreationForm(forms.Form):
#    copies = forms.IntegerField(required=True)
#    license_type = forms.ChoiceField(choices=CUSTOM_CHOICES)    
    
class CreationForm(forms.Form):

    def __init__(self,custom_choices,*args,**kwargs): 
        super(CreationForm,self).__init__(*args,**kwargs)  
        #import pdb; pdb.set_trace()

      
#        self.fields['license_type'].choices = {('L1','L1'),('L2','L2'),('L5','L5'),('U1','U1'),('U3','U3'),('U6','U6')}
#       self.fields['license_type'].choices = custom_choices
        self.fields['license_type'] = forms.ChoiceField( choices=custom_choices  )
 
    copies = forms.IntegerField(required=True)
    license_type=forms.ChoiceField()
    
    
