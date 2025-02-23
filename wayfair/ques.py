# Problem Statement:
#     Given a the following set of data set, create a function that will find the coupon to display for a given category.
# Coupons = [
# ]
# {"CategoryName":"Comforter Sets", "CouponName":"Comforters Sale"},
# {"CategoryName":"Bedding", "CouponName":"Savings on Bedding"}, {"CategoryName":"Bed & Bath", "CouponName": "Low price for Bed & Bath"}
# Categories [
# ]
# {"CategoryName":"Comforter Sets", "CategoryParentName":"Bedding"}, {"CategoryName":"Bedding", "CategoryParentName": "Bed & Bath"},
# {"CategoryName":"Bed & Bath", "CategoryParentName":null},
# {"CategoryName":"Soap Dispensers", "CategoryParentName":"Bathroom Accessories"}, {"CategoryName":"Bathroom Accessories", "CategoryParentName":"Bed & Bath"}, {"CategoryName":"Toy Organizers", "CategoryParentName":"Baby And Kids"}, {"CategoryName":"Baby And Kids", "CategoryParentName":null}
# # tests: input (CategoryName) => output (CouponName)
# "Comforter Sets"
# "Bedding"
# => "Comforters Sale"
# => "Savings on Bedding"
# "Bathroom Accessories" => "Low price for Bed & Bath"
# "Soap Dispensers"
# "Toy Organizers"
# => "Low price for Bed & Bath"
# => null

coupons = [
    {"CategoryName":"Comforter Sets", "CouponName":"Comforters Sale"},
    {"CategoryName":"Bedding", "CouponName":"Savings on Bedding"},
    {"CategoryName":"Bed & Bath", "CouponName": "Low price for Bed & Bath"}
]

categories = [
    {"CategoryName":"Comforter Sets", "CategoryParentName":"Bedding"},
    {"CategoryName":"Bedding", "CategoryParentName": "Bed & Bath"},
    {"CategoryName":"Bed & Bath", "CategoryParentName": None},
    {"CategoryName":"Soap Dispensers", "CategoryParentName":"Bathroom Accessories"},
    {"CategoryName":"Bathroom Accessories", "CategoryParentName":"Bed & Bath"},
    {"CategoryName":"Toy Organizers", "CategoryParentName":"Baby And Kids"},
    {"CategoryName":"Baby And Kids", "CategoryParentName": None}
]

def find_coupon(category_name):
    # Build a dictionary for quick lookup of category's parent
    category_to_parent = {category["CategoryName"]: category["CategoryParentName"] for category in categories}
    
    # Build a dictionary for quick lookup of coupon by category
    category_to_coupon = {coupon["CategoryName"]: coupon["CouponName"] for coupon in coupons}
    
    current_category = category_name
    
    # Traverse up the hierarchy looking for a matching coupon
    while current_category is not None:
        if current_category in category_to_coupon:
            return category_to_coupon[current_category]
        else:
            current_category = category_to_parent.get(current_category, None)
    
    # If no coupon is found throughout the hierarchy
    return None

# Testing the function with the provided test cases
print(find_coupon("Comforter Sets")) # "Comforters Sale"
print(find_coupon("Bedding")) # "Savings on Bedding"
print(find_coupon("Bathroom Accessories")) # "Low price for Bed & Bath"
print(find_coupon("Soap Dispensers")) # "Low price for Bed & Bath"
print(find_coupon("Toy Organizers")) # None


# Problem Statement:
#     The findBestCoupon function is being called billions of times per day while not being a core feature of the site. Can you make the function faster?
# Instructions
# Copy and Paste the solution from Part 2 as a starting point to work through this exercise.
# Requirements/Acceptance Criteria:
# • All Requirements from prior question
# • Code should still pass all of the same prior test cases
# • O(n) is not fast enough come up with a O(1) solution!

# Assuming 'categories' and 'coupons' are defined as before

# Maps each category to its parent
category_parent_map = {cat['CategoryName']: cat['CategoryParentName'] for cat in categories}

# Maps each category to its directly associated coupon, if any
category_coupon_map = {coupon['CategoryName']: coupon['CouponName'] for coupon in coupons}

# This function pre-computes the best coupon for each category
def pre_compute_best_coupon():
    best_coupon_map = {}
    
    # Helper function to find and cache the best coupon for a category
    def find_and_cache_best_coupon(category):
        if category in best_coupon_map:  # If already computed, return it
            return best_coupon_map[category]
        
        if category in category_coupon_map:  # Direct coupon association
            best_coupon_map[category] = category_coupon_map[category]
            return category_coupon_map[category]
        
        parent_category = category_parent_map.get(category)
        if parent_category:
            # Recursively find the best coupon from the parent and cache it
            best_coupon = find_and_cache_best_coupon(parent_category)
            best_coupon_map[category] = best_coupon
            return best_coupon
        else:
            # No parent and no direct coupon, hence no best coupon
            best_coupon_map[category] = None
            return None
    
    # Compute and cache the best coupon for all categories
    for category in category_parent_map.keys():
        find_and_cache_best_coupon(category)
    
    return best_coupon_map

# Pre-compute the best coupon for each category
best_coupon_map = pre_compute_best_coupon()

# Now, the findBestCoupon function has O(1) complexity
def findBestCoupon(category_name):
    return best_coupon_map.get(category_name)

# Testing the optimized function with the same test cases
print(findBestCoupon("Comforter Sets"))  # Expected: "Comforters Sale"
print(findBestCoupon("Bedding"))  # Expected: "Savings on Bedding"
print(findBestCoupon("Bathroom Accessories"))  # Expected: "Low price for Bed & Bath"
print(findBestCoupon("Soap Dispensers"))  # Expected: "Low price for Bed & Bath"
print(findBestCoupon("Toy Organizers"))  # Expected: None
