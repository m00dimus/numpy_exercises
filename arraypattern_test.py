import unittest
import numpy
from numpy.testing import assert_

from arraypatterns import *

class TestDiamond(unittest.TestCase):
    def testdiamond_defaultvalues(self):
        """ Test the diamond pattern using default values """
        want=np.array((1.))
        got=diamondarray()
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_defaultvalues_2(self):
        """ Test the diamond pattern using using defined input values """
        want=np.array((1.))
        dimensionsize=1
        fillvalue=1
        unfillvalue=0
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_defaultvalues_3(self):
        """ Test the diamond pattern using default input values with larger dimension"""
        want=np.array([(0.,1.,0.),(1.,0.,1.),(0.,1.,0.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=0
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_even_dimension(self):
        """ Test the diamond pattern using even dimension"""
        want=np.array([
        (0.,0.,1.,1.,0.,0.),
        (0.,1.,0.,0.,1.,0.),
        (1.,0.,0.,0.,0.,1.),
        (1.,0.,0.,0.,0.,1.),
        (0.,1.,0.,0.,1.,0.),
        (0.,0.,1.,1.,0.,0.),
        ])
        dimensionsize=6
        got=diamondarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_larger_even_dimension(self):
        """ Test the diamond pattern using a larger even dimension"""
        want=np.array([
        (0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,),
        (0.,0.,0.,0.,1.,0.,0.,1.,0.,0.,0.,0.,),
        (0.,0.,0.,1.,0.,0.,0.,0.,1.,0.,0.,0.,),
        (0.,0.,1.,0.,0.,0.,0.,0.,0.,1.,0.,0.,),
        (0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,1.,0.,),
        (1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,1.,),
        (1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,1.,),
        (0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,1.,0.,),
        (0.,0.,1.,0.,0.,0.,0.,0.,0.,1.,0.,0.,),
        (0.,0.,0.,1.,0.,0.,0.,0.,1.,0.,0.,0.,),
        (0.,0.,0.,0.,1.,0.,0.,1.,0.,0.,0.,0.,),
        (0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,),
        ])
        dimensionsize=12
        got=diamondarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_invalid_string_dimension(self):
        """ Test the diamond pattern using invalid string dimension"""
        want=np.array([(0.)])
        dimensionsize='one'
        got=diamondarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_fill_values(self):
        """ Test the diamond pattern using using custom fill value """
        want=np.array((9.))
        dimensionsize=1
        fillvalue=9
        unfillvalue=0
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_fill_values2(self):
        """ Test the diamond pattern using using custom fill value for larger array """
        want=np.array([(0.,88.,0.),(88.,0.,88.),(0.,88.,0.)])
        dimensionsize=3
        fillvalue=88
        unfillvalue=0
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_unfill_values(self):
        """ Test the diamond pattern using using custom unfill value for larger array """
        want=np.array([(99.,1.,99.),(1.,99.,1.),(99.,1.,99.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=99
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_fill_float_values(self):
        """ Test the diamond pattern using using custom fill float value for larger array """
        want=np.array([(0.,77.1,0.),(77.1,0.,77.1),(0.,77.1,0.)])
        dimensionsize=3
        fillvalue=77.1
        unfillvalue=0
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_unfill_float_values(self):
        """ Test the diamond pattern using using custom unfill float value for larger array """
        want=np.array([(99.2,1.,99.2),(1.,99.2,1.),(99.2,1.,99.2)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=99.2
        got=diamondarray(dimension=dimensionsize,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

class TestBisector(unittest.TestCase):
    def testbisector_defaultvalues(self):
        """ Test the bisector pattern using default values """
        want=np.array((1.))
        got=bisectorarray()
        numpy.testing.assert_array_equal(got,want)

    def testdiamond_defaultvalues_2(self):
        """ Test the bisector pattern using using defined input values """
        want=np.array((1.))
        dimensionsize=1
        fillvalue=1
        unfillvalue=0
        verticalstate=False
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_larger_array(self):
        """ Test the bisector pattern using default input values with larger dimension"""
        want=np.array([(0.,1.,0.),(1.,1.,1.),(0.,1.,0.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=0
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_larger_array_vertical_off(self):
        """ Test the bisector pattern using default input values vertical off and larger dimension"""
        want=np.array([(0.,0.,0.),(1.,1.,1.),(0.,0.,0.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=0
        verticalstate=False
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_larger_array_horizontal_off(self):
        """ Test the bisector pattern using default input values vertical off and larger dimension"""
        want=np.array([(0.,1.,0.),(0.,1.,0.),(0.,1.,0.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=0
        verticalstate=True
        horizontalstate=False
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_even_dimension(self):
        """ Test the bisector pattern using even dimension"""
        want=np.array([
        (0.,1.,1.,0.),
        (1.,1.,1.,1.),
        (1.,1.,1.,1.),
        (0.,1.,1.,0.)
        ])
        dimensionsize=4
        got=bisectorarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_larger_even_dimension(self):
        """ Test the bisector pattern using larger even dimension"""
        want=np.array([
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.),
        (1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        (0.,0.,0.,0.,0.,0.,1.,1.,0.,0.,0.,0.,0.,0.),
        ])
        dimensionsize=14
        got=bisectorarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_invalid_string_dimension(self):
        """ Test the bisector pattern using invalid string dimension"""
        want=np.array([(0.)])
        dimensionsize='one'
        got=bisectorarray(dimensionsize)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_fill_values(self):
        """ Test the bisector pattern using using custom fill value """
        want=np.array((9.))
        dimensionsize=1
        fillvalue=9
        unfillvalue=0
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_fill_values2(self):
        """ Test the bisector pattern using using custom fill value for larger array """
        want=np.array([(0.,88.,0.),(88.,88.,88.),(0.,88.,0.)])
        dimensionsize=3
        fillvalue=88
        unfillvalue=0
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_unfill_values(self):
        """ Test the bisector pattern using using custom unfill value for larger array """
        want=np.array([(99.,1.,99.),(1.,1.,1.),(99.,1.,99.)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=99
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_fill_float_values(self):
        """ Test the bisector pattern using using custom fill float value for larger array """
        want=np.array([(0.,77.1,0.),(77.1,77.1,77.1),(0.,77.1,0.)])
        dimensionsize=3
        fillvalue=77.1
        unfillvalue=0
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

    def testbisector_unfill_float_values(self):
        """ Test the bisector pattern using using custom unfill float value for larger array """
        want=np.array([(99.2,1.,99.2),(1.,1.,1.),(99.2,1.,99.2)])
        dimensionsize=3
        fillvalue=1
        unfillvalue=99.2
        verticalstate=True
        horizontalstate=True
        got=bisectorarray(dimension=dimensionsize,vertical=verticalstate,horizontal=horizontalstate,fill=fillvalue,unfill=unfillvalue)
        numpy.testing.assert_array_equal(got,want)

def TestAll():
	""" Run all unittests """
	unittest.main(verbosity=2)
	sys.exit()

def main():
	""" Main Function """
	testall = True

	if testall:
		TestAll()

if __name__ == "__main__":
	main()
