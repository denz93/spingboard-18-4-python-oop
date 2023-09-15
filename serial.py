"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start: int):
        """
        :param start: int
        """
        self.start = start
        self.counter = 0

    def generate(self) -> int:
        """Generate next serial number
        :return: int
        """
        next = self.start + self.counter
        self.counter += 1
        return next 
    def reset(self):
        """Reset the counter to 0

        """
        self.counter = 0
    
    def __repr__(self) -> str:
        return f"<SerialGenerator start={self.start+self.counter} next={self.start+self.counter+1}>"
    

