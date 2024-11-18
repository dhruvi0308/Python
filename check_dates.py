from hw10pr1 import Date

if __name__ == '__main__':
    """First complete the constructor method of the Date class, 
        then run this program and check the results incrementally,
        as you develop more methods. 
        Feel free to add more dates and method calls.
    """
    date1 = Date(11, 16, 2022)
    print("date1: ", date1)

    date2 = Date(2, 27, 2020)
    print("date2: ", date2)

    print("is date1 before date2? should be False -- ", 
            date1.is_before(date2))

    print("date1 is in a leap year? should be False -- ", 
            date1.is_leap_year())

    print("date2 is in a leap year? should be True -- ",  
            date2.is_leap_year())

    print() #print an empty line before the next part
    print("date2 advancing, first by one day")
    date2.advance_one_day()
    print("date2 should be 02/28/2020")
    print(date2)

    print("... then by 4 days,")
    print("as displayed by 02/28/2020 and its subsequent four days")
    date2.advance_print_n_days(4)

    print("date2 now, should be 03/03/2020")
    print(date2)

    print() #print an empty line before the next part
    date3 = date2.copy()
    print("date3, created as a copy of date2")
    print(date3)
    print("date3, advance and print 0 days in addition to its current date")
    date3.advance_print_n_days(0)