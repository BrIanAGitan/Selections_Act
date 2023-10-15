# ChineseYear Zodiac Calendar
Rat = 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020
Ox = 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021
Tiger = 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022
Rabbit = 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023
Dragon = 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024
Snake = 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025
Horse = 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026
Goat = 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027
Monkey = 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028
Rooster = 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029
Dog = 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030
Pig = 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031
# Input
year = eval(input("What is your Birth year?"))

# If Else Statement And Display Result
if year in Rat:
    print("Your Chinese Zodiac sign is Rat.")
elif year in Ox:
    print("Your Chinese Zodiac sign is Ox.")
elif year in Tiger:
    print("Your Chinese Zodiac sign is Tiger.")
elif year in Rabbit:
    print("Your Chinese Zodiac sign is Rabbit.")
elif year in Dragon:
    print("Your Chinese Zodiac sign is Dragon.")
elif year in Snake:
    print("Your Chinese Zodiac sign is Snake.")
elif year in Horse:
    print("Your Chinese Zodiac sign is Horse.")
elif year in Goat:
    print("Your Chinese Zodiac sign is Goat.")
elif year in Monkey:
    print("Your Chinese Zodiac sign is Monkey.")
elif year in Rooster:
    print("Your Chinese Zodiac sign is Rooster.")
elif year in Dog:
    print("Your Chinese Zodiac sign is Dog.")
elif year in Pig:
    print("Your Chinese Zodiac sign is Pig.")
else:
    print("I Dunno man we haven't gotten there yet.The scope of our calendar is between 1924 - 2031")
