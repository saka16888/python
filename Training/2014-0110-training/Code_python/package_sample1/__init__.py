print 'importing package_sample1'

from module_a import function1
from module_b import function2
from sub_package.module_c import SampleClass

CurrentTemperature = 90


__all__ = [
    'function1',
    'CurrentTemperature',
]
