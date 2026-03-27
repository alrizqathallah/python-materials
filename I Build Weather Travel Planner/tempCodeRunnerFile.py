# Defining Variables
distance_mi = 2.5           # Boolean
is_raining = True          # Boolean
has_bike = False             # Boolean
has_car = False             # Boolean
has_ride_share_app = True   # Boolean

# CONDITIONAL LOGIC
if not distance_mi: # Checking condition of disctance_mi, and make sure value is not Falsy or 0.
  print(False)      # Print False, if the value of distance_mi is Falsy value.
elif distance_mi <= 1:   # checking condition, distance less than 1 mile
  if not is_raining:     # if not raining (true)
    print(True)
  else:                  # if raining (false)
    print(False)
elif distance_mi >= 1:   # checking condition, distance more than 1 mile, and less than 6 mile.
  if has_bike and not is_raining:    # if has bike and not raining, true
    print(True)
  else:                              # if has bike but is raining, false
    print(False)
else:             # distance greater than 6 mile.
  if has_car or has_ride_share_app:
    print(True)
  else:
    print(False)
