from testbook import testbook
import numpy as np

def test_values():
    with testbook('2_IntelliSense.ipynb', execute=True) as tb:
        array1 = tb.value('array1[0]')
        assert np.isclose(array1, 4.0), f"array1[0]={array1} of task 3.1 is not equal to 4"

        newtext = tb.ref('newtext')
        assert newtext == "hello MUDE", f"newtext={newtext} of task 3.2 is not equal to 'hello MUDE'"
