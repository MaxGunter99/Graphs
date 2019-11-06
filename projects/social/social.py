import random
import os
os.system( 'clear' )

print( '\n' )

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:

    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """

        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # call addUser() until our number of users is numUsers

        for i in range(numUsers):

            self.addUser(f"User {i+1}")

        # Create random friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships

        possibleFriendships = []

        # Avoid dupes by ensuring the first ID is smaller than the second

        for userID in self.users:

            for friendID in range(userID + 1, self.lastID + 1):

                possibleFriendships.append( (userID, friendID) )

        # Shuffle the list

        random.shuffle(possibleFriendships)
        # print("Random Friendships:")
        # print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships

        totalFriendships = avgFriendships * numUsers // 2
        # print(f"Friendships to create: {totalFriendships}\n")

        for i in range(totalFriendships):

            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Relationships => {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        # paths to each relation => {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

        visited = {}  # Note that this is a dictionary, not a set

        print( '\nFind paths from:' , userID )

        queue = []

        # queue copies of the current path

        if self.friendships[ userID ] == set():

            print( 'This individual has no friends.☹️' )
            return None

        else:

            visited.update({ userID : self.friendships[ userID ] })

        queue.append( userID )

        temp = userID
        visit = []

        while len( queue ) >= 1:

            temp = queue[0]
            visit.append( temp )
            print( '\ntemp' , temp )

            for i in self.friendships[ queue[0] ]:

                if i in visited:

                    # print( f'{i} in visited' )
                    None

                else:

                    if len( visit ) > 2:
                        if visit[ len( visit ) - 1 ] in self.friendships[ visit[ len( visit ) - 3 ] ]:
                            if visit[ len( visit ) - 2 ] in self.friendships[ visit[ len( visit ) - 3 ] ]:
                                visit.pop( len( visit ) - 2 )
                                print( visit , i )

                    else:        

                        print( visit , i )
                        queue.append( i )
                        visited.update({ i : self.friendships[ i ] })

            queue.pop( 0 )

        # print( 'PATH' , paths )
        print( 'Queue' , queue )
        print( 'Visited' , visited )
        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print( 'Users:' , sg.users )
    print( 'Friendships:' , sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
