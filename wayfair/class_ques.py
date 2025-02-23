from datetime import datetime

class CouponFinder:
    def __init__(self, categories, coupons):
        self.categories = categories
        self.coupons = {coupon['CategoryName']: coupon for coupon in sorted(coupons, key=lambda x: datetime.strptime(x['DateModified'], '%Y-%m-%d'), reverse=True)}
        self.category_parent_map = {cat['CategoryName']: cat['CategoryParentName'] for cat in categories}
        # Initialize the best_coupon_map to store the most applicable coupon for each category.
        print(self.coupons, '-----coupon')
        print(self.category_parent_map, '-----category')
        self.best_coupon_map = {}
        self._initialize_best_coupon_map()

    def _initialize_best_coupon_map(self):
        # Precompute the best coupon for each category, considering hierarchy.
        for category in self.category_parent_map:
            self._find_and_cache_best_coupon(category)

    def _find_and_cache_best_coupon(self, category):
        # Look for the best applicable coupon for a category, considering its hierarchy.
        if category in self.best_coupon_map:  # If already computed, return it.
            return self.best_coupon_map[category]

        coupon = self.coupons.get(category)
        if coupon:
            self.best_coupon_map[category] = coupon
            return coupon

        parent_category = self.category_parent_map.get(category)
        if parent_category:
            best_coupon = self._find_and_cache_best_coupon(parent_category)
            self.best_coupon_map[category] = best_coupon
            return best_coupon
        else:
            self.best_coupon_map[category] = None
            return None

    def apply_coupon(self, category_name, original_price):
        """Applies the best coupon for the given category to the original price."""
        coupon = self.find_best_coupon(category_name)
        if not coupon:
            return original_price  # No coupon found, return original price
        
        discount = coupon['Discount']
        if discount.endswith('%'):
            discount_rate = float(discount.rstrip('%')) / 100
            new_price = original_price * (1 - discount_rate)
        elif discount.startswith('$'):
            discount_amount = float(discount.lstrip('$'))
            new_price = original_price - discount_amount
        else:
            return original_price  # Unrecognized discount format
        
        return max(new_price, 0)  # Ensure the new price is not negative

    def find_best_coupon(self, category_name):
        """Returns the most applicable coupon dictionary for a given category."""
        return self.best_coupon_map.get(category_name)



# Example usage:
coupons = [
{ "CategoryName":"Comforter Sets", "CouponName":"Comforters Sale", "DateModified":"2020-01-01", "Discount": "10%"},
{ "CategoryName":"Comforter Sets", "CouponName":"Cozy Comforter Coupon", "DateModified":"2020-01-01", "Discount": "$15"},
{ "CategoryName":"Bedding", "CouponName":"Best Bedding Bargains", "DateModified":"2019-01-01", "Discount": "35%"},
{ "CategoryName":"Bedding", "CouponName":"Savings on Bedding", "DateModified":"2019-01-01", "Discount": "25%"},
{ "CategoryName":"Bed & Bath", "CouponName":"Low price for Bed & Bath", "DateModified":"2018-01-01", "Discount": "50%"},
{ "CategoryName":"Bed & Bath", "CouponName":"Bed & Bath extravaganza", "DateModified":"2019-01-01", "Discount": "75%"}
]
categories = [
{"CategoryName":"Comforter Sets", "CategoryParentName":"Bedding"},
{"CategoryName":"Bedding", "CategoryParentName":"Bed & Bath"},
{"CategoryName":"Bed & Bath", "CategoryParentName":None},
{"CategoryName":"Soap Dispensers", "CategoryParentName":"Bathroom Accessories"},
{"CategoryName":"Bathroom Accessories", "CategoryParentName":"Bed & Bath"},
{"CategoryName":"Toy Organizers", "CategoryParentName":"Baby And Kids"}, 
{"CategoryName":"Baby And Kids", "CategoryParentName":None}
]

coupon_finder = CouponFinder(categories, coupons)

# Testing the class method
print(coupon_finder.find_best_coupon("Comforter Sets"))  # Expected: "Comforters Sale"
print(coupon_finder.find_best_coupon("Bedding"))  # Expected: "Savings on Bedding"
print(coupon_finder.find_best_coupon("Bathroom Accessories"))  # Expected: "Low price for Bed & Bath"
print(coupon_finder.find_best_coupon("Soap Dispensers"))  # Expected: "Low price for Bed & Bath"
print(coupon_finder.find_best_coupon("Toy Organizers"))  # Expected: None
