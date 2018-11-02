

'''Command-line test runner

   (pyATS3) $python easypy.py test_sim_better device_name=pyats-asa-2

'''

import sys
import aetest

test_module_name = sys.argv[1]
test_module = __import__(test_module_name)

parameters = {}
for pair in sys.argv[2:]:
    key, value = pair.split('=')
    if value.isdecimal():
        value = int(value)
    parameters[key] = value

testcases = []
for name in dir(test_module):
    obj = getattr(test_module, name)
    if isinstance(obj, type) and issubclass(obj, aetest.Testcase):
        testcases.append(obj())

aetest.main(testcases, **parameters)


