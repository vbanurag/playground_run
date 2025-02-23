from dataclasses import abc

class Test:
    test = 3

    def __str__(self):
        """
        Returns a string representation of the object.

        Parameters:
            self (object): The object to be represented as a string.

        Returns:
            str: The string representation of the object.
        """
        return f"{self.__class__.__name__} {self.test}"
# end 


print(Test())