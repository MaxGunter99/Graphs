import os
os.system( 'clear' )

#     10
#     /
#    1   2   4  11
#     \ /   / \ /
#      3   5   8
#       \ / \   \
#        6   7   9

def earliest_ancestor(ancestors, starting_node):

    # Format ( 10 , 1 )
    # Ancestor ^    ^ Child

    parents = []

    print( '\n\n-=-=-=-= Start from:' , starting_node , '=-=-=-=-' )

    # Loop through ancestors
    for i in ancestors:

        # Add first ancestor to the starting node
        if i[1] == starting_node:
            parents.append( i[0] )

        # If there are already added ancestors
        if len( parents ) >= 1:
            
            # compare them
            if parents[ len( parents ) - 1 ] == i[1]:
                parents.append( i[0] )


        elif i[0] == starting_node:
            # print( 'start' , i )
            parents.append( i[0] )

    # In case I missed any
    for i in parents:

        for x in ancestors:

            if i == x[1]:

                parents.append( x[0] )

    noDupes = []
    index = 0

    # Scan for dupes
    for i in parents:
        
        if i in noDupes:
            print( 'Duplicate' )
            parents.pop( index )
            index += 1

        else:
            noDupes.append( i )
            index += 1

    split = []

    # check for the same child and return smaller of the two parents
    for i in ancestors:

            # If there are two ancestors
            if len( parents ) == 2:

                # Add [ parent , child ] to split
                if parents[0] == i[0]:
                    # print( f' {parents[0]}s Child is {i[1]}' )
                    split.append( [ parents[0] , i[1] ] )

                # Add [ parent , child ] to split
                elif parents[1] == i[0]:
                    # print( f' {parents[1]}s Child is {i[1]}' )
                    split.append( [ parents[1] , i[1] ] )

    # Look through split and compare if the 
    for i in range( len( split ) - 1 ):

        # If the current parent has the same child as the next parent, return the smaller number
        if split[i][1] == split[ i + 1 ][1]:

            if split[i][0] >= split[ i + 1 ][0]:
                return split[ i + 1 ][0]

            else:
                return split[ i ][0]
        


    print( 'Parents:' , parents )
    print( 'Parents are from different generations' )

    if len( split ) > 0:
        print( '\n-----------------------------------' )
        print( 'SPLIT' , split )
        print( '-----------------------------------' )

    # if there are more than 2 ancestors from different generations, return the last ( oldest )
    if len( parents ) >= 2:
        return parents[ len( parents ) - 1 ]

    # If no ancestors, return -1
    else:
        return -1