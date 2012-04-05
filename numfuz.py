class NumFuzz():
    """
    This is a very basic number fuzzer.
    the idea is to use permutations of factors of 2.
    The permutations, or extended methods are for added alteration of the possible digits returned.
    This data can be fed to something else.
    returns of all methods are generators
    """

    def fuznumber(self):
        """
        this method returns a fuzzing that contains all the numbers from the simple sets
        """
        result = []
        for i in self.doubles(): result.append(i)
        for i in self.doubles_extended(): result.append(i)
        for i in result: yield i

    def doubles(self):
        """
        This returns simply powers of two
        """
        result = [
                0x00000001,
                0x00000010,
                0x00000100,
                0x00001000,
                0x00010000,
                0x00100000,
                0x01000000,
                0x10000000,
                0x20000000,
                0x40000000,
                0x60000000,
                0x80000000,
                0x100000000,
                ]
        for item in result: yield item

    def doubles_extended(self):
        """
        This method returns powers of two permutated
        """
        result = []
        for i in self._doubles():
            result.append(i + 1)
            result.append(i + 2)
            result.append(i - 1)
            result.append(i - 2 )
            result.append(i * -1 )
            result.append((i  + 1) * -1)
            result.append((i + 2) * -1)
        for item in result: yield item
