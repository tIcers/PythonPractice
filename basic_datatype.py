import os

# variable and simple data type
name = "Eric"
message = f"Hello {name}, would you like to learn python today?"
print(message)

upper_message = f"Hello {name.upper()}, would you like to learn python today?"
print(upper_message)

lower_message = f"Hello {name.lower()}, would you like to learn python today?"
formatted_message = f"Hello {name.title()}, would you like to learn python today?"
print(lower_message)
print(formatted_message)

person = "Ichiro Suzuki"
quote = f"{person}: 小さなことを重ねることがとんでもないところに行く ただひとつの道"
print(quote)

person_name = " Ichiro Suzuki "
formatted_name = person_name.rstrip()
formatted_name_2 = person_name.lstrip()
formatted_name_3 = person_name.strip()
print(f"\t{formatted_name}\n\t{formatted_name_2}\n\t{formatted_name_3}")

# numbers
addition = 5 + 3
sb = 11 - 3
div = 16 // 2
mul = 4 * 2
print(addition, sb, div, mul)

favorite_number = 7
favonum_message = f"{favorite_number} is considered lucky number"
print(favonum_message)

