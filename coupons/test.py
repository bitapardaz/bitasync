def test(): 
    from django.contrib.auth.models import User
    from user_profile.models import UserProfile,CustomerProfile
    from coupons.models import B2C_Coupon

    user = User.objects.get(username='normalcustomer')
    user_profile = UserProfile.objects.get(user=user)
    customer_profile = CustomerProfile.objects.get(user_profile = user_profile)

    import datetime
    now = datetime.datetime.now()

    new_coupon = B2C_Coupon(Expiery_data= now.date(),Discount_rate=0.2) 
    new_coupon.save()
