from django.contrib import admin
from .models import Data_Transfer_Plan
from .models import Contact_Comment
from .models import Purchase

# Register your models here.
admin.site.register(Data_Transfer_Plan)
admin.site.register(Contact_Comment)
admin.site.register(Purchase)
