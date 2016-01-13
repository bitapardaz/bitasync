from django.dispatch import receiver
from utilities.utility_functions import generate_md5_hash

def pending_purchase_created(sender, instance, created, **kwargs):

    if created:
        hashcode = generate_md5_hash(str(instance.id))
        instance.hashcode = hashcode
        instance.save()
