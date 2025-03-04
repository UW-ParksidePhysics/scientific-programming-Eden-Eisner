def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    return (5/9)*(fahrenheit_temperature-32)

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9/5)*(celsius_temperature+32)

# Test Temps for Celsius
test_temp_celsius = [0 ,21, 100]


#Table header
print(f"{'Celsius' :>10} {'Fahrenheit' :>15} {'Converted back' :>20}")

# Making the table
for temp_c in test_temp_celsius:
    temp_f = convert_celsius_temperature_to_fahrenheit(temp_c)
    converted_back = convert_fahrenheit_temperature_to_celsius(temp_f)
    print(f"{temp_c:>10} {temp_f:15} {converted_back:>20}")