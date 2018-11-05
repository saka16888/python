# 1st useage
#import Package1
#print("\ndir(Package1) \n",dir(Package1))

#from Package1.Package2 import *

'''
from Package1 import module1
from Package1 import Package2
import Packag1.module1
import Packag1.Package2
'''

#Package1.module1.test_m11()
from Package1 import *
print("\ndir(module1) \n",dir(module1))
module1.test_m11()
module1.test_m12()

module2.test_m21()
module2.test_m22()

#from Package1.Package2 import module1, module2
from Package1.Package2 import module1
print("\ndir(Package2) \n",dir(Package2))
module1.test_p2_m1_11()
module1.test_p2_m1_12()

from Package1.Package2 import module2
print("\ndir(Package2) \n",dir(module2))
module2.test_p2_m2_11()
test_p2_m2_11()