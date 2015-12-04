import hashlib

def generate_md5_hash(input_string): 
    hasher = hashlib.md5()   
    hasher.update(input_string)
    return hasher.hexdigest()
            
            
def create_temp_plan(plan,coupons):
    # a TempPlan is simply a plan, but with the additional data 
    # about the pricing given the customer coupons 
        
    temp_plan = TempPlan()
    temp_plan.plan_name = plan.plan_name
    temp_plan.original_price = plan.price
    temp_plan.image_link = get_plan_image_link(plan.plan_name)
    temp_plan.long_description = plan.long_description 

    if coupons: 
        (best_coupon,discounted_price) = calculate_discounted_price(plan,coupons)
        temp_plan.discounted_price = discounted_price   

    return temp_plan   
    
    
def calculate_discounted_price(plan,coupons): 
    # returns a tuple (current_coupon,discounted_price) where current_coupon 
    # is the coupon which is most favorable for the customer, 
    # and discounted_price is the price after applying the most favorable coupon. 
    
    # get the best coupon: the coupon with largest discount rate 
    current_coupon = coupons[0]
    best_coupon = current_coupon
    for current_coupon in coupons: 
        if current_coupon.discount_rate >= best_coupon.discount_rate : 
            best_coupon = current_coupon    
               
    # apply the coupon to the prices 
    discounted_price =  plan.price * best_coupon.discount_rate                                    
    return (best_coupon,discounted_price)    
    
    
class TempPlan(): 
    
    def __init__(self):  
                   
        self.plan_name = ""
        self.original_price = 0
        self.discounted_price = 0
        self.image_link = ""
        self.long_description = ""
        
        
def get_plan_image_link(plan_name): 

    plan_image_link = dict([ ('L1',''), 
                             ('L3',''),  
                             ('L6',''), 
                             ('U1',''), 
                             ('U3',''), 
                             ('U6',''), 
                        ])
                        
    return  plan_image_link[plan_name]
