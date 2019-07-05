import numpy as np

def diamondarray(dimension=1,fill=1,unfill=0):
    """ Create a diamond array using a square dimension.
    Fill and unfill values can be integer or float. """
    nullresult=np.zeros(1)

    #// verify inputs
    try:
        if not isinstance(dimension, (int, np.integer)):
            dimesion=int(dimension)
        if not isinstance(fill, (int, float, np.integer)):
            fill=int(fill)
        if not isinstance(unfill, (int, float, np.integer)):
            unfill=int(unfill)
    except:
        return nullresult

    #// check if odd

        return nullresult

    #// initialize 2d array
    a=np.zeros((dimension,dimension))

    for row in range(dimension):
        for col in range(dimension):
            a[row,col]=unfill

    #// find the middle of the array
    midpoint=(dimension-1)/2

    #// initialize an offset
    offset=-1
    offsetstep=1

    #// loop through rows and columns
    for row in range(dimension):
        if dimension%2 == 0 and row == np.ceil(midpoint):
            #// repeat offset for second midpoint row
            offset=offset
        else:
            if row <= np.ceil(midpoint):
                #// increase offset for each row for top
                offset=offset+offsetstep
            else:
                #// decrease offset for each row for bottom
                offset=offset-offsetstep

        for col in range(dimension):
            #// set value to one
            if dimension%2 == 0:
                if col <= np.floor(midpoint):
                    if col == np.floor(midpoint)-offset:
                        a[row,col]=fill
                if col >= np.ceil(midpoint):
                    if col == int(midpoint)+offset+1:
                        a[row,col]=fill
            else:
                if col == midpoint+offset or col == midpoint-offset:
                    pass
                    a[row,col]=fill
    return a

def bisectorarray(dimension=1,vertical=True,horizontal=True,fill=1,unfill=0):
    """ Create an array using square dimension with the midpoint column
    filled. Fill and unfill values can be integer or float. """

    nullresult=np.zeros(1)

    #// verify inputs
    try:
        if not isinstance(dimension, (int, np.integer)):
            dimesion=int(dimension)
        if not isinstance(fill, (int, float, np.integer)):
            fill=int(fill)
        if not isinstance(unfill, (int, float, np.integer)):
            unfill=int(unfill)
    except:
        return nullresult

    #// initialize 2d array
    a=np.zeros((dimension,dimension))

    for row in range(dimension):
        for col in range(dimension):
            a[row,col]=unfill

    #// find the middle of the array
    midpoint=(dimension-1)/2

    #// loop through rows and columns
    for row in range(dimension):
        for col in range(dimension):
            #// set value to one
            if (col == np.floor(midpoint) or col == np.ceil(midpoint)) and vertical==True:
                a[row,col]=fill
            if (row == np.floor(midpoint) or row == np.ceil(midpoint)) and horizontal==True:
                a[row,col]=fill
    return a
