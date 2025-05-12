distance_to_school = 35.4 #kilometers
test_distance = .64 #kilometers

kilometers_to_centimeters = .00001
centimeter_to_inch = 0.393701
inch_to_foot = (1/12)
foot_to_yard = (1/3)
yard_to_mile = 0.000568182

print(f" {distance_to_school/kilometers_to_centimeters*centimeter_to_inch} inches,"
      f" {distance_to_school/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot} feet,"
      f" {distance_to_school/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot*foot_to_yard} yards, "
      f" {distance_to_school/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot*foot_to_yard*yard_to_mile} miles")

print(f" {test_distance/kilometers_to_centimeters*centimeter_to_inch} inches,"
      f" {test_distance/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot} feet,"
      f" {test_distance/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot*foot_to_yard} yards, "
      f" {test_distance/kilometers_to_centimeters*centimeter_to_inch*inch_to_foot*foot_to_yard*yard_to_mile} miles")