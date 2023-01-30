""" Task 1
Briefly describe a possible collection of classes which can be used to represent a music collection
(for example, inside a music player), focusing on how they would be related by composition.
You should include classes for songs, artists, albums and playlists. Hint: write down the four class names,
draw a line between each pair of classes which you think should have a relationship,
and decide what kind of relationship would be the most appropriate.

For simplicity, you can assume that any song or album has a single “artist” value
(which could represent more than one person), but you should include compilation albums
(which contain songs by a selection of different artists). The “artist” of a compilation album can be a special
value like “Various Artists”. You can also assume that each song is associated with a single album,
but that multiple copies of the same song (which are included in different albums) can exist.

Write a simple implementation of this model which clearly shows how the different classes are composed.
Write some example code to show how you would use your classes to create an album and add all its songs to a playlist.
Hint: if two objects are related to each other bidirectionally, you will have to decide how this link
should be formed – one of the objects will have to be created before the other,
so you can’t link them to each other in both directions simultaneously.
"""


""" Task 2
A very common use case for inheritance is the creation of a custom exception hierarchy. 
Because we use the class of an exception to determine whether it should be caught by a particular except block, 
it is useful for us to define custom classes for exceptions which we want to raise in our code. 
Using inheritance in our classes is useful because if an except block catches a particular exception class, 
it will also catch its child classes (because a child class is its parent class). 
That means that we can efficiently write except blocks which handle groups of related exceptions, 
just by arranging them in a logical hierarchy. Our exception classes should inherit from Python’s built-in 
exception classes. They often won’t need to contain any additional attributes or methods.

Write a simple program which loops over a list of user data (tuples containing a username, email and age) 
and adds each user to a directory if the user is at least 16 years old. You do not need to store the age. 
Write a simple exception hierarchy which defines a different exception for each of these error conditions:
1. the username is not unique
2. the age is not a positive integer
3. the user is under 16
4. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)

Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move 
onto the next set of data in the list. Print a different error message for each different kind of exception.

Think about where else it would be a good idea to use a custom class, 
and what kind of collection type would be most appropriate for your directory.

You can consider an email address to be valid if it contains one @ symbol and has a non-empty username and domain name – 
you don’t need to check for valid characters. You can assume that the age is already an integer value.
"""
