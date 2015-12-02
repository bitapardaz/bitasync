import hashlib

def generate_md5_hash(input_string): 
    hasher = hashlib.md5()   
    hasher.update(input_string)
    return hasher.hexdigest()
        
def products_original_prices():

    prices = dict([('L1', get_price("L1")),
                   ('L3', get_price("L3")),
                   ('L6', get_price("L6")),
                   ('U1', get_price("U1")),
                   ('U3', get_price("U3")),
                   ('U6', get_price("U6")) ])
    return prices 
   
def product_discounted_price(coupons): 
    # returns a tuple (current_coupon,discounted_price) where current_coupon 
    # is the coupon which is most favorable for the customer, 
    # and discounted_price is a dictionary where current_coupon is utilised. 
    
    # get the best coupon: the coupon with largest discount rate 
    current_coupon = coupons[0]
    best_coupon = current_coupon
    for current_coupon in coupons: 
        if current_coupon.discount_rate >= best_coupon.discount_rate : 
            best_coupon = current_coupon    
               
    # apply the coupon to the prices 
    discounted_prices = dict([ ('L1', get_price("L1") * best_coupon.discount_rate ), 
                                      ('L3', get_price("L3") * best_coupon.discount_rate ),
                                      ('L6', get_price("L6") * best_coupon.discount_rate ),
                                      ('U1', get_price("U1") * best_coupon.discount_rate ),
                                      ('U3', get_price("U3") * best_coupon.discount_rate ),
                                      ('U6', get_price("U6") * best_coupon.discount_rate )
                                    ])
                                    
    return (best_coupon,discounted_price)
    
    
def get_price(plan_name):
    if plan_name  == "L1": 
        return 2000 
    elif plan_name == "L3":
        return 3000
    elif plan_name == "L6": 
        return 5000
    elif plan_name == "U1": 
        return 8000
    elif plan_name == "U3": 
        return 150000
    elif plan_name == "U6": 
        return 250000
        
