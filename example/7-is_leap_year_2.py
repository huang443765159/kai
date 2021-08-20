def is_leap_year(year):
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
        else:
            result = True
    return result


def search_leap_year(year_start, year_end):
    # Found the 1st Leap Year
    leap_year_1st = int()
    for this_year in range(year_start, year_end, 1):
        is_leap = is_leap_year(this_year)
        if is_leap:
            leap_year_1st = this_year
            break

    # Found other Leap Year
    for this_year in range(leap_year_1st, year_end, 4):
        print('Leap Year =', this_year)


search_leap_year(0, 400)
