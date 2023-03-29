import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = "+91"
number += input("Enter your Number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
valid = phonenumbers.is_valid_number(phone);
print(number)
print(time)
print(car)
print(reg)
if(valid):
    print("yes the number is valid")
else:
    print("No the number is not valid")
