from django.dispatch import receiver
from utilities.utility_functions import generate_md5_hash

def b2c_coupon_created(sender, instance, created, **kwargs):

    # the instance is a b2c_coupon
    if created: 
        hashcode = generate_md5_hash(str(instance.id))
        instance.save()
    
