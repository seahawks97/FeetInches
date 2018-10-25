"""
Steven Tucker
14 October 2018
CSC 231-003, Fall 2018
Lab 2: Foot Measure Project
"""

class FootMeasure:
    def __init__(self, feet = 0, inches = 0):
        """Initializes the FootMeasure object upon creation. Validates the input to make sure it is a valid input
        i.e. neither feet nor inches are negative. Initializes private operators __feet and __cents to be
        feet and inches, respectively."""
        self.__feet = feet                                  # Sets private __feet to feet
        self.__inches = inches                              # Sets private __inches to inches
        self.validate(feet, inches)                         # Validates the Measurement

    def validate(self, feet, inches):
        """If feet or inches are negative, a value is raised because it is not a valid measurement. If it is a valid
        measurement, 'Valid input' is printed."""
        if feet < 0 or inches < 0:
            raise ValueError('Negative Measurement Error: Measurement must be greater than or equal to 0.')
        if inches > 11:                                     # 12 inches would be 1 foot
            self.__feet = self.roundFeet(feet, inches)      # Rounds feet up
            self.__inches = self.roundInches(inches)        # Rounds inches up

            # Printing Statements
            # print('new feet: ' + str(self.__feet))
            # print('new inches: ' + str(self.__inches))
            new_measure = FootMeasure(self.__feet, self.__inches)   # Returns a new object with updated values
            return new_measure

    def getFeet(self):
        """Public access variable for private variable __feet."""
        return self.__feet

    def getInches(self):
        """Public access variable for private variable __inches."""
        return self.__inches

    def roundFeet(self, feet, inches):
        """In case that inches runs over 11, this updates the feet to be the floor division of 12.
        Sets the object's __feet equal to the floor division, then returns it."""
        feet += inches // 12
        self.__feet = feet
        return self.__feet

    def roundInches(self, inches):
        """In case that inches runs over 11, this updates the inches to be the remainder of 12.
        Sets the object's __inches equal to the remainder, then returns it."""
        # print('raw inches in: ' + str(inches))
        # print('modulo: ' + str(inches % 12))
        new_in = inches % 12
        self.__inches = new_in
        return self.__inches

    def __str__(self):
        """Standard format of printing the measurement object."""
        # return str(self.__feet) + ' ft. ' + str(self.__inches) + ' in.'
        return self.__repr__()

    def __repr__(self):
        """Returns inches higher than 11 as a combo measurement (i.e. 68 inches is shown as '5 ft. 8 in.', NOT '68 in.'
        Returns just the foot measurement if it is an even measurement (i.e. 60 inches is represented as '5 ft.',
        NOT '5 ft. 0 in.' Returns 0 overall as 0 ft. 0 in."""
        if self.__inches == 0 and self.__feet == 0:
            return '0 ft. 0 in.'
        elif self.__feet == 0:
            return str(self.__inches) + ' in.'
        elif self.__inches == 0:
            return str(self.__feet) + ' ft.'
        else:
            return str(self.__feet) + ' ft. ' + str(self.__inches) + ' in.'

    def __add__(self, rMeasure):
        """Adds the feet together, then adds the inches together. Returns a new instance of FeetMeasure."""
        f3 = self.getFeet() + rMeasure.getFeet()
        i3 = self.getInches() + rMeasure.getInches()
        return FootMeasure(f3, i3)

    def __eq__(self, other):
        """Both feet and inches must match to be equivalent."""
        if self.getFeet() == other.getFeet() and self.getInches() == other.getInches():
            return True
        else:
            return False

    def __ne__(self, other):
        """Faster to evaluate than calling __eq__, comparing them, and then returning the not.
        Also, an OR statement is faster to evaluate because only 1 statement has to be false."""
        if self.getFeet() != other.getFeet() or self.getInches() != other.getInches():
            return True
        else:
            return False

    def __lt__(self, other):
        """Compares if the self (1st) instance is < the other (2nd)"""
        f1 = self.getFeet()
        f2 = other.getFeet()
        if f1 < f2:
            return True
        elif f1 == f2:
            if self.getInches() < other.getInches():
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        """Compares if the self (1st) instance is <= the other (2nd)"""
        f1 = self.getFeet()
        f2 = other.getFeet()
        if f1 < f2:
            return True
        elif f1 == f2:
            if self.getInches() <= other.getInches():
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        """Compares if the self (1st) instance is > the other (2nd)"""
        f1 = self.getFeet()
        f2 = other.getFeet()
        if f1 > f2:
            return True
        elif f1 == f2:
            if self.getInches() > other.getInches():
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        """Compares if the self (1st) instance is >= the other (2nd)"""
        f1 = self.getFeet()
        f2 = other.getFeet()
        if f1 > f2:
            return True
        elif f1 == f2:
            if self.getInches() >= other.getInches():
                return True
            else:
                return False
        else:
            return False