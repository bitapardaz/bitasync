from django.dispatch import receiver
from utilities.utility_functions import generate_md5_hash

def coupon_created(sender, instance, created, **kwargs):


    if created: 
        print (instance.id)
        hashcode = generate_md5_hash(str(instance.id))
        instance.hashcode = hashcode
        instance.save()
    
