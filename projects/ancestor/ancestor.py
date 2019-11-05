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

    print( '\n ---------------- \n' )

    # Format ( 10 , 1 )
    # Ancestor ^    ^ Child

    parents = []

    print( 'Start from:' , starting_node )

    for i in ancestors:

        if i[1] == starting_node:
            parents.append( i[0] )

        if len( parents ) >= 1:
            
            if parents[ len( parents ) - 1 ] == i[1]:
                parents.append( i[0] )


        elif i[0] == starting_node:

            print( 'start - ' , i )

            parents.append( i[0] )

    print( 'Parents:' , parents )

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


    print( 'Parents:' , parents )

    # if len( parents ) == 2:
    #     return parents[0]

    if len( parents ) >= 2:
        return parents[ len( parents ) - 1 ]

    else:
        return -1