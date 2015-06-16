#-------------------------------------------------------------------------------
# Name:        calender.py
# Purpose:     print the calender of the given year
#
# Author:      Akshay
#
# Created:     11-06-2015
#-------------------------------------------------------------------------------

DAYS_OF_THE_WEEK = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
MONTHS_OF_THE_YEAR = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DAYS_IN_MONTH = (31,28,31,30,31,30,31,31,30,31,30,31)

def is_leap_year(y):
    return (y%4 == 0) and (not (y%100 == 0) or y%400 == 0)

def get_day_of_the_week(pos):
    return DAYS_OF_THE_WEEK(pos)

def day_for_date(d, m, y):
    """Return number corresponding to day of the week for given date. Month is 0-11."""
    assert 0 <= m <= 11
    assert 0 < d <= DAYS_IN_MONTH[m]
    assert 1800 <= y <= 2999

    century_digits = y//100
    year_digits = y%100
    value = year_digits + year_digits//4

    if century_digits == 18:
        value += 2

    if century_digits == 20:
        value += 6

    if m == 0 and not is_leap_year(y): #Jan and NOT a leap year
        value += 1
    elif m == 1 and is_leap_year(y): #Feb + Leap year
        value += 3
    elif m == 1 and not is_leap_year(y): #Feb
        value += 4
    elif m == 2 or m == 10: #March and November
        value += 4
    elif m == 4: #May
        value += 2
    elif m == 5: #june
        value += 5
    elif m == 7: #Aug
        value += 3
    elif m == 9: #Oct
        value += 1
    elif m == 8 or m == 11: #Sept or Dec
        value += 6

    value += (d-1)
    value = (value+7)%7
    return value

def print_calender_month(m, y):
    """Month is 1-12"""
    m -= 1 #Work with 0-11
    assert 0 <= m <= 11
    assert 1800 <= y <= 2999

    s = ''
##    list_repr = []
##    s_prime = ''
##    #Print the title
    print('{} {}'.format(MONTHS_OF_THE_YEAR[m],y))
    s += '{} {}'.format(MONTHS_OF_THE_YEAR[m],y)
##    s_prime += '{} {}'.format(MONTHS_OF_THE_YEAR[m],y)
##    list_repr.append('{0:^27}'.format(s_prime))
##    s_prime = ''
    s += '\n'
##
    for day in DAYS_OF_THE_WEEK:
        print(day,end=' ')
        s += (day + ' ')
##        s_prime += (day + ' ')
    s = s.strip()
##    s_prime = s_prime.strip()
    print()
##    list_repr.append(s_prime)
##    s_prime = ''

    s += '\n'
    first_of_month = day_for_date(1,m,y)
    i = 0
    count = 0
    while i < first_of_month:
        print(' '*3, end = ' ')
##        s_prime += ' '*3
##        s_prime += ' '
        s += ' '*3
        s += ' '
        count += 1
        i += 1

    i = 1
    days_in_this_month = DAYS_IN_MONTH[m]
    if is_leap_year(y) and m == 1:
        days_in_this_month += 1

    while i <= days_in_this_month:
        #i holds the date being currently printed.
        if count > 6:
            print()

##            list_repr.append(s_prime.rstrip())
##            s_prime = ''
            s = s[:-1] +'\n'
            count = 0
##
        print('{0:>3}'.format(i), end = ' ')
        s += '{0:>3}'.format(i)
##        s_prime += '{0:>3}'.format(i)
##        s_prime += ' '
        s += ' '
        i += 1
        count += 1
##
    print()
    s = s[:-1]
##    if s_prime:
##        if len(s_prime) < 27:
##            s_prime += ' '*(27 - len(s_prime))
##
##        list_repr.append(s_prime)
##
##    if len(list_repr) < 8:
##        while len(list_repr) < 8:
##            list_repr.append(' '*27)
##
##    return list_repr
    lines = s.split('\n')
    lines[0] = '{0:^27}'.format(lines[0])
    print(lines)
    for line in lines:
        print(len(line))
    return s



def get_calender_month(m, y):
    """Month is 1-12"""
    m -= 1 #Work with 0-11
    assert 0 <= m <= 11
    assert 1800 <= y <= 2999

##    s = ''
    list_repr = []
    s_prime = ''
    #Print the title
##    print('{} {}'.format(MONTHS_OF_THE_YEAR[m],y))
##    s += '{} {}'.format(MONTHS_OF_THE_YEAR[m],y)
    s_prime += '{} {}'.format(MONTHS_OF_THE_YEAR[m],y)
    list_repr.append('{0:^27}'.format(s_prime))
    s_prime = ''
##    s += '\n'

    for day in DAYS_OF_THE_WEEK:
##        print(day,end=' ')
##        s += (day + ' ')
        s_prime += (day + ' ')
##    s = s.strip()
    s_prime = s_prime.strip()
##    print()
    list_repr.append(s_prime)
    s_prime = ''
##    s += '\n'
    first_of_month = day_for_date(1,m,y)
    i = 0
    count = 0
    while i < first_of_month:
##        print(' '*3, end = ' ')
        s_prime += ' '*3
        s_prime += ' '
##        s += ' '*3
##        s += ' '
        count += 1
        i += 1

    i = 1
    days_in_this_month = DAYS_IN_MONTH[m]
    if is_leap_year(y) and m == 1:
        days_in_this_month += 1

    while i <= days_in_this_month:
        #i holds the date being currently printed.
        if count > 6:
##            print()

            list_repr.append(s_prime.rstrip())
            s_prime = ''
##            s += '\n'
            count = 0

##        print('{0:>3}'.format(i), end = ' ')
##        s += '{0:>3}'.format(i)
        s_prime += '{0:>3}'.format(i)
        s_prime += ' '
##        s += ' '
        i += 1
        count += 1

    if s_prime:
        if len(s_prime) < 27:
            s_prime += ' '*(27 - len(s_prime))
        elif len(s_prime) >= 28:
            s_prime = s_prime[:27]
        list_repr.append(s_prime)

    if len(list_repr) < 8:
        while len(list_repr) < 8:
            list_repr.append(' '*27)

    return list_repr



def print_calender_year(y):
    """Return a list of lists, each inner list containing a list of strings for the calender of a single month."""
    assert 1800 <= y <= 2999, 'Choose a year between 1800 and 2999 only.'

    print('{0:^117}'.format(y))
    print()
    p = []

    #Call each month, format and print.
    for i in range(12):
        p.append(get_calender_month(i+1,y))


##    for q in p:
##        print(q[0])
##        for x in q[1:]:
##            print(len(x), end = ' ')
##        print()

##    assert False

    for j in range(3):
        for k in range(len(p[0])):
            for i in range(4):
                print(p[j*4 + i][k], end = ' '*3)
            print()
        print()


def get_int(prompt, low = None,high = None):
    """Return the user-inputted integer between low and high (inclusive)."""

    assert (low == None or high == None) or low <= high
    done = False
    x = None
    while not done:
        x = int(input(prompt))
        flag1 = False
        flag2 = False
        if low is not None:
            if x < low:
                print('Sorry, the number must be greater than {}.'.format(low))
            else:
                flag1 = True
        else:
            flag1 = True

        if high is not None:
            if x > high:
                print('Sorry, the number must be greater than {}.'.format(high))
            else:
                flag2 = True
        else:
            flag2 = True

        if flag1 and flag2:
            done = True

    return x



def main():
    year = get_int('Welcome to the calender centre. \n Enter a year between 1800 and 2999 for the calender of that year. ', 1800, 2999)
    print_calender_year(year)


if __name__ == '__main__':
    main()
