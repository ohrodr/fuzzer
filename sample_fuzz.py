"""
   I would expect this not to work.
   I wanted to provide a very basic example of number fuzz

"""

import os
import numfuz

nf = numfuz.NumFuzz()
output = []
for item in nf.doubles():
    cmd_string = 'tail -%s /var/log/messages' %( item )
    output.extend(os.popen(cmd_string).readlines())

print '\n'.join(output)
