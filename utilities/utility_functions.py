import hashlib

def generate_md5_hash(input_string): 
    hasher = hashlib.md5()   
    hasher.update(input_string)
    return hasher.hexdigest()
            

class TempPlan(): 
    
    def __init__(self):  
                   
        self.plan_name = ""
        self.original_price = 0
        self.discounted_price = 0
        self.image_link = ""
        self.description = ""
        self.long_description = ""            
            
def create_temp_plan(plan,coupons):
    # a TempPlan is simply a plan, but with the additional data (discounted_price)
    # given the customer coupons 
        
    temp_plan = TempPlan()
    temp_plan.plan_name = plan.plan_name
    temp_plan.original_price = plan.price
    temp_plan.image_link = get_plan_image_link(plan.plan_name)
    temp_plan.description = plan.description
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
    best_coupon = get_best_coupon(coupons)
               
    # apply the coupon to the prices 
    discounted_price =  int(plan.price * ( 1 - best_coupon.discount_rate))
    return (best_coupon,discounted_price)  
    
    
def get_best_coupon(coupons): 

    current_coupon = coupons[0]
    best_coupon = current_coupon
    
    for current_coupon in coupons: 
        if current_coupon.discount_rate >= best_coupon.discount_rate : 
            best_coupon = current_coupon   
     
    return best_coupon             

    
def get_plan_by_name(all_plans, fname): 
    for plan in all_plans:
        if plan.plan_name == fname :  
            return plan     

        
def get_plan_image_link(plan_name): 

    plan_image_link = dict([ ('L1','/static/bitasync_site/img/L1.jpg'), 
                             ('L2','/static/bitasync_site/img/L2.jpg'),  
                             ('L5','/static/bitasync_site/img/L5.jpg'), 
                             ('U1','/static/bitasync_site/img/U1.jpg'), 
                             ('U3','/static/bitasync_site/img/U3.jpg'), 
                             ('U6','/static/bitasync_site/img/U6.jpg'), 
                        ])
                        
    return  plan_image_link[plan_name]
