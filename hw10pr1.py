class Date:
    """A class that stores and manipulates dates, represented by int month, day, and year."""

    def __init__(self, month_param, day_param, year_param):
        """The constructor for the Date class. Initializes attributes -- month, day, year, using the parameters."""
        self.month = month_param
        self.day = day_param
        self.year = year_param

    def __repr__(self):
        """Returns a string representation for the calling Date object, i.e., self."""
        s = f'{self.month:02d}/{self.day:02d}/{self.year:04d}'
        return s

    def is_before(self, other):
        """Returns True if self is a date before other."""
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                return self.day < other.day
        return False

    def is_leap_year(self):
        """Returns True if the calling date, referred to as self, is in a leap year. Otherwise, returns False."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def advance_one_day(self):
        """Advances the calling object, i.e., self, by 1 day, without printing anything."""
        days_in_month = [0, 31, 28 + self.is_leap_year(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day < days_in_month[self.month]:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

    def advance_print_n_days(self, n):
        """Advances the calling object self by n >= 0 days, also prints the starting date and its subsequent n days."""
        print(self)
        for _ in range(n):
            self.advance_one_day()
            print(self)

    def copy(self):
        """Returns a new object with the same month, day, year as the calling object (self)."""
        new_date = Date(self.month, self.day, self.year)
        return new_date