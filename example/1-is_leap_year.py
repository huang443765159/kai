def is_leap_year(year):
    active = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                active = True
        else:
            active = True
    else:
        active = False
    return active


def search_leap_year(year_s, year_e):
    for one_year in range(year_s, year_e+1):
        critical_result = is_leap_year(year=one_year)
        if critical_result is True:
            print(f'leap year is {one_year}')


search_leap_year(1800, 2000)
