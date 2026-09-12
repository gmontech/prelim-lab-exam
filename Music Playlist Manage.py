
# ============================================================
# PART II - MUSIC PLAYLIST MANAGER
# DATA STRUCTURE: SINGLY LINKED LIST ADT
# ============================================================


# ============================================================
# SONG CLASS
# ============================================================

# Create a class named Song.
# This class stores the information of one song.
class Song:

    # This is the constructor.
    # It runs automatically whenever we create a new Song.
    def __init__(self, song_id, song_title, artist, duration):

        # Store the Song ID inside the object.
        self.song_id = song_id

        # Store the Song Title inside the object.
        self.song_title = song_title

        # Store the Artist name inside the object.
        self.artist = artist

        # Store the Song Duration inside the object.
        self.duration = duration

    # This method displays the information of the song.
    def display(self):

        # Display the Song ID.
        print("Song ID    :", self.song_id)

        # Display the Song Title.
        print("Song Title :", self.song_title)

        # Display the Artist.
        print("Artist     :", self.artist)

        # Display the Duration.
        print("Duration   :", self.duration)


# ============================================================
# NODE CLASS
# ============================================================

# Create a Node class.
# A node contains the song data and a link to the next node.
class Node:

    # Constructor for the Node.
    def __init__(self, song):

        # Store the Song object inside the node.
        self.data = song

        # Set the next link to None.
        # None means that the node is not connected to another node yet.
        self.next = None


# ============================================================
# SINGLY LINKED LIST ADT
# ============================================================

# Create our own LinkedList class.
# This class manages all the nodes in the playlist.
class LinkedList:

    # Constructor for the LinkedList.
    def __init__(self):

        # head points to the first node in the list.
        # At the beginning, there are no nodes.
        self.head = None

        # count keeps track of how many songs are in the playlist.
        self.count = 0


    # ========================================================
    # IS EMPTY
    # ========================================================

    # This method checks if the playlist is empty.
    def is_empty(self):

        # If head is None, there is no first node.
        # Therefore, the playlist is empty.
        return self.head is None


    # ========================================================
    # SIZE
    # ========================================================

    # This method returns the number of songs.
    def size(self):

        # Return the current value of count.
        return self.count


    # ========================================================
    # INSERT FIRST
    # ADD SONG AT THE BEGINNING
    # ========================================================

    # This method adds a song at the beginning of the playlist.
    def insert_first(self, song):

        # Create a new node containing the song.
        new_node = Node(song)

        # Make the new node point to the current first node.
        new_node.next = self.head

        # Make the new node become the new first node.
        self.head = new_node

        # Increase the number of songs by 1.
        self.count += 1

        # Tell the user that the song was successfully added.
        print("Song added at the beginning.")


    # ========================================================
    # INSERT LAST
    # ADD SONG AT THE END
    # ========================================================

    # This method adds a song at the end of the playlist.
    def insert_last(self, song):

        # Create a new node containing the song.
        new_node = Node(song)

        # Check if the playlist is empty.
        if self.head is None:

            # If empty, the new node becomes the first node.
            self.head = new_node

        else:

            # Start at the first node.
            current = self.head

            # Continue moving until we reach the last node.
            while current.next is not None:

                # Move current to the next node.
                current = current.next

            # The last node now points to the new node.
            current.next = new_node

        # Increase the number of songs by 1.
        self.count += 1

        # Tell the user that the song was added.
        print("Song added at the end.")


    # ========================================================
    # INSERT AT SPECIFIC POSITION
    # ========================================================

    # This method inserts a song at a specific position.
    # Positions start at 1.
    def insert_at(self, song, position):

        # Check if the position is valid.
        # The position can be from 1 up to count + 1.
        if position < 1 or position > self.count + 1:

            # Display an error message if the position is invalid.
            print("Invalid position.")

            # Stop the method.
            return

        # If the position is 1,
        # the song should be inserted at the beginning.
        if position == 1:

            # Call the insert_first method.
            self.insert_first(song)

            # Stop the method because the insertion is finished.
            return

        # If the position is count + 1,
        # the song should be inserted at the end.
        if position == self.count + 1:

            # Call the insert_last method.
            self.insert_last(song)

            # Stop the method.
            return

        # Create a new node containing the song.
        new_node = Node(song)

        # Start at the first node.
        current = self.head

        # Move current to the node BEFORE the desired position.
        for i in range(1, position - 1):

            # Move to the next node.
            current = current.next

        # Connect the new node to the node that was originally next.
        new_node.next = current.next

        # Connect the previous node to the new node.
        current.next = new_node

        # Increase the number of songs by 1.
        self.count += 1

        # Display a success message.
        print("Song inserted at position", position)


    # ========================================================
    # SEARCH SONG
    # SEARCH USING SONG ID
    # ========================================================

    # This method searches for a song using its Song ID.
    def search(self, song_id):

        # Start searching from the first node.
        current = self.head

        # Continue until there are no more nodes.
        while current is not None:

            # Compare the Song ID in the current node
            # with the ID entered by the user.
            #
            # lower() makes the search case-insensitive.
            if current.data.song_id.lower() == song_id.lower():

                # Return the Song object if it is found.
                return current.data

            # Move to the next node.
            current = current.next

        # Return None if the song was not found.
        return None


    # ========================================================
    # DELETE SONG
    # REMOVE USING SONG ID
    # ========================================================

    # This method removes a song using its Song ID.
    def delete(self, song_id):

        # Check if the playlist is empty.
        if self.head is None:

            # Return False because there is nothing to delete.
            return False

        # Check if the first node contains the Song ID.
        if self.head.data.song_id.lower() == song_id.lower():

            # Move head to the second node.
            #
            # The first node is now removed from the list.
            self.head = self.head.next

            # Decrease the number of songs.
            self.count -= 1

            # Return True because deletion was successful.
            return True

        # Start at the first node.
        current = self.head

        # Continue while there is another node after current.
        while current.next is not None:

            # Check if the NEXT node contains the Song ID.
            if current.next.data.song_id.lower() == song_id.lower():

                # Skip the node that will be deleted.
                #
                # Example:
                # A -> B -> C
                #
                # After this:
                # A -> C
                current.next = current.next.next

                # Decrease the number of songs.
                self.count -= 1

                # Return True because deletion was successful.
                return True

            # Move to the next node.
            current = current.next

        # Return False if the Song ID was not found.
        return False


    # ========================================================
    # DISPLAY PLAYLIST
    # ========================================================

    # This method displays all songs in the playlist.
    def display(self):

        # Check if the playlist is empty.
        if self.head is None:

            # Tell the user that there are no songs.
            print("\nPlaylist is empty.")

            # Stop the method.
            return

        # Start at the first node.
        current = self.head

        # Position counter starts at 1.
        position = 1

        # Display the playlist header.
        print("\n================================")
        print("         MUSIC PLAYLIST")
        print("================================")

        # Traverse the linked list.
        # Continue until current becomes None.
        while current is not None:

            # Display the position of the song.
            print("\nPosition:", position)

            # Display a separator.
            print("-------------------------------")

            # Display the song information.
            current.data.display()

            # Move to the next node.
            current = current.next

            # Increase the position by 1.
            position += 1

        # Display the total number of songs.
        print("\n================================")
        print("Total Songs:", self.count)
        print("================================")


# ============================================================
# INPUT SONG INFORMATION
# ============================================================

# This function asks the user for the song information.
def input_song():

    # Ask the user for the Song ID.
    song_id = input("Enter Song ID: ")

    # Ask the user for the Song Title.
    song_title = input("Enter Song Title: ")

    # Ask the user for the Artist.
    artist = input("Enter Artist: ")

    # Ask the user for the Duration.
    duration = input("Enter Duration: ")

    # Create a Song object using the information entered.
    return Song(song_id, song_title, artist, duration)


# ============================================================
# CREATE THE PLAYLIST
# ============================================================

# Create an object of our LinkedList class.
# This will be our music playlist.
playlist = LinkedList()


# ============================================================
# MAIN PROGRAM / MENU
# ============================================================

# Use an infinite loop to keep showing the menu.
while True:

    # Display the menu.
    print("\n================================")
    print("     MUSIC PLAYLIST MANAGER")
    print("================================")

    # Menu option 1.
    print("1. Add Song at Beginning")

    # Menu option 2.
    print("2. Add Song at End")

    # Menu option 3.
    print("3. Insert Song at Position")

    # Menu option 4.
    print("4. Display Playlist")

    # Menu option 5.
    print("5. Search Song")

    # Menu option 6.
    print("6. Remove Song")

    # Menu option 7.
    print("7. Display Playlist Size")

    # Menu option 8.
    print("8. Exit")

    # Display another separator.
    print("================================")

    # Ask the user to select an option.
    choice = input("Enter your choice: ")


    # ========================================================
    # OPTION 1 - ADD AT BEGINNING
    # ========================================================

    if choice == "1":

        # Display the operation title.
        print("\n--- Add Song at Beginning ---")

        # Ask for the song information.
        song = input_song()

        # Add the song at the beginning.
        playlist.insert_first(song)


    # ========================================================
    # OPTION 2 - ADD AT END
    # ========================================================

    elif choice == "2":

        # Display the operation title.
        print("\n--- Add Song at End ---")

        # Ask for the song information.
        song = input_song()

        # Add the song at the end.
        playlist.insert_last(song)


    # ========================================================
    # OPTION 3 - INSERT AT POSITION
    # ========================================================

    elif choice == "3":

        # Display the operation title.
        print("\n--- Insert Song at Position ---")

        # Try to convert the position entered into an integer.
        try:

            # Ask the user for the position.
            position = int(input("Enter position: "))

            # Ask for the song information.
            song = input_song()

            # Insert the song at the selected position.
            playlist.insert_at(song, position)

        # If the user enters something that is not a number,
        # a ValueError will occur.
        except ValueError:

            # Display an error message.
            print("Please enter a valid number.")


    # ========================================================
    # OPTION 4 - DISPLAY PLAYLIST
    # ========================================================

    elif choice == "4":

        # Display all songs in the playlist.
        playlist.display()


    # ========================================================
    # OPTION 5 - SEARCH SONG
    # ========================================================

    elif choice == "5":

        # Display the operation title.
        print("\n--- Search Song ---")

        # Ask the user for the Song ID.
        song_id = input("Enter Song ID: ")

        # Search for the song.
        song = playlist.search(song_id)

        # Check if a song was found.
        if song is not None:

            # Display the success message.
            print("\nSong Found!")

            # Display a separator.
            print("-------------------------------")

            # Display the song information.
            song.display()

        # If song is None, it was not found.
        else:

            # Display the not-found message.
            print("\nSong not found.")


    # ========================================================
    # OPTION 6 - REMOVE SONG
    # ========================================================

    elif choice == "6":

        # Display the operation title.
        print("\n--- Remove Song ---")

        # Ask the user for the Song ID to remove.
        song_id = input("Enter Song ID to remove: ")

        # Call the delete method.
        removed = playlist.delete(song_id)

        # Check if the deletion was successful.
        if removed:

            # Display success message.
            print("Song removed successfully.")

        # If removed is False, the song was not found.
        else:

            # Display not-found message.
            print("Song not found.")


    # ========================================================
    # OPTION 7 - DISPLAY PLAYLIST SIZE
    # ========================================================

    elif choice == "7":

        # Display the operation title.
        print("\n--- Playlist Size ---")

        # Call the size method and display the result.
        print("Total number of songs:", playlist.size())


    # ========================================================
    # OPTION 8 - EXIT
    # ========================================================

    elif choice == "8":

        # Display a message before exiting.
        print("\nThank you for using Music Playlist Manager!")

        # Break stops the while loop.
        break


    # ========================================================
    # INVALID OPTION
    # ========================================================

    else:

        # Display an error message if the choice is invalid.
        print("\nInvalid choice. Please try again.")
