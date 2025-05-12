def convert_list_of_tuples(star_data):
    """
    Converts a list of tuples containing star data into a nested dictionary.

    Args:
        star_data (list of tuples): Each tuple contains the star's name, distance,
                                     apparent brightness, and luminosity.

    Returns:
        dict: A nested dictionary where the key is the star's name and the value is a
              dictionary with 'distance', 'apparent brightness', and 'luminosity'.
    """
    stars = {}

    for star in star_data:
        name, distance, apparent_brightness, luminosity = star
        stars[name] = {
            'distance': distance,
            'apparent brightness': apparent_brightness,
            'luminosity': luminosity
        }

    return stars


def print_star_information(star_name, stars):
    """
    Prints out information about a specific star from the nested dictionary.

    Args:
        star_name (str): The name of the star.
        stars (dict): The nested dictionary of star data.
    """
    if star_name in stars:
        star_info = stars[star_name]
        print(f"Star: {star_name}")
        print(f"    Distance (ly):            {star_info['distance']}")
        print(f"    Apparent brightness (m):  {star_info['apparent brightness']}")
        print(f"    Luminosity (L_sun):       {star_info['luminosity']}")
    else:
        print(f"Star '{star_name}' not found.")


# Data
nearby_star_data = [
    ('Alpha Centauri A', 4.3, 0.26, 1.56),
    ('Alpha Centauri B', 4.3, 0.077, 0.45),
    ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
    ("Barnard's Star", 6.0, 0.00004, 0.0005),
    ('Wolf 359', 7.7, 0.000001, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
    ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
    ('Sirius A', 8.6, 1.00, 23.6),
    ('Sirius B', 8.6, 0.001, 0.003),
    ('Ross 154', 9.4, 0.00002, 0.0005),
]

# Convert the list of tuples into a nested dictionary
stars = convert_list_of_tuples(nearby_star_data)

# Print information about two stars
print_star_information('Alpha Centauri A', stars)
print_star_information('Sirius B', stars)
