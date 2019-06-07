    c1 = ComplexNumber(2,3)
    del c1.imag
    c1.getData()
Traceback (most recent call last):

# AttributeError: 'ComplexNumber' object has no attribute 'imag'

    del ComplexNumber.getData
    c1.getData()
Traceback (most recent call last):

# AttributeError: 'ComplexNumber' object has no attribute 'getData