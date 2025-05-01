average_life_expectancy = 77.5 #years

one_billion_seconds = 1_000_000_000 #seconds

one_billion_seconds_in_years = (one_billion_seconds/60/60/24/365)

if one_billion_seconds_in_years >= average_life_expectancy:
    print(f"Yes, a newborn baby can expect to live for a billion seconds as it equals {round(one_billion_seconds_in_years, 1)}, which is greater then the average life expectancy of {average_life_expectancy} years")
else:
    print(f"No, a newborn baby can not expect to live for a billion seconds as it equals {round(one_billion_seconds_in_years,1)}, which is less then the average life expectancy of {average_life_expectancy} years")