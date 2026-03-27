# Function Apply Discount

# defining function
def apply_discount(price, discount): # Takes two parameters (price and discount)
  # Checking if price not a number (integer or float)
  if type(price) not in (int, float):
    return 'The price should be a number'
  # Checking if discount not a number (integer or float)
  if not isinstance(discount, (int, float)):
    return 'The discount should be a number'
  # checking if price less than 0, must be greater than 0
  if price <= 0:
    return 'The price should be greater than 0'
  # checking if discount less than 0, and more than 100, must be between 0 and 100.
  if discount < 0 or discount > 100:
    return 'The discount should be between 0 and 100'
  # Final calculation
  final_price = price * (1 - discount / 100)
  '''
  20/100 = 0.20
  1 - 0.20 = 0.80
  100 * 0.80 = 80
  '''
  return final_price    # 80

print(apply_discount(100, 20))   # 80