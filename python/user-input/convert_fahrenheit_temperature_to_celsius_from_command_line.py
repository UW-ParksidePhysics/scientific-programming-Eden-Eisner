def fahenheit_to_celcius(temp_f):
    return (temp_f - 32) * (5 / 9)

if __name__ == '__main__':
    temp_in_fahrenheit = int(input("What is the Temperature in Fahrenheit: "))

    print(temp_in_fahrenheit,", ", fahenheit_to_celcius(temp_in_fahrenheit))