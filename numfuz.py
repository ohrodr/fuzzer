###
#   Author  : Robb Driscoll
#   License : GPLv3
#   Email   : ohrodr@gmail.com
#   Date    : 4/5/12
###

class NumFuzz():
    """
    This is a very basic number fuzzer.
    The idea is to use permutations of factors of 2.
    The permutations, or extended methods are for added alteration of the possible digits returned.
    This data can be fed to something else.
    returns of all methods are generators

    USAGE:
        >>> import numfuz
        >>> nf = numfuz.NumFuzz()
        >>> nf.fuznumber()
        <generator object fuznumber at 0xb728f02c>
        >>> for i in nf.fuznumber(): print i
        ...
        >>> for i in nf.doubles(): print i
        ...
        >>> for i in nf.doubles_extended(): print i
        ...

    """

    def fuznumber(self):
        """
        This method returns a fuzzing that contains all the numbers from associated methods
        return is generator
        """
        result = []
        # append self.doubles() output
        for i in self.doubles(): result.append(i)
        # append self.doubles_extended() output
        for i in self.doubles_extended(): result.append(i)
        for i in result: yield i

    def doubles(self):
        """
        This returns simply powers of two
        return is generator
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
        return is generator
        """
        result = []
        for i in self.doubles():
            result.append(i + 1)
            result.append(i + 2)
            result.append(i - 1)
            result.append(i - 2 )
            result.append(i * -1 )
            result.append((i  + 1) * -1)
            result.append((i + 2) * -1)
        for item in result: yield item
