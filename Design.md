# Initial Draft 

## Problem Statement 
There is a library ABC that hosts over 10,000 books and scholarly articles that can be accessed physically and digitally respectively. The library also has several visitors, but only a handful of librarians to attend to the visitors’ requests. This is not an efficient library management system since there is too much load on the librarians when the number of visitors increases. Therefore, a system that simulates the presence of a librarian performing the tasks that is requested by a user is an optimal solution to this problem. In other words, an intelligent bot that understands the user’s requests and responds to the queries that the user would otherwise pose to a human librarian, in a way that a human librarian would respond is a practical solution that caters to the needs of the librarian as well as the users of the library. In addition to giving a hand to the librarians in assisting the visitors, the bot also offers a special feature that a human might find it difficult to perform. The bot also assists the users in what source or material they are looking for in the cases that the users are not sure about what they are looking for but only have an idea. 
## Bot Description
The bot designed to assist the users in their requests can perform all the tasks that a human librarian would do. The user can chat with the bot in the same way that they would with a human librarian and pose their queries or requests. 

The bot should be able to issue books, accept the returned books and organize them back, accordingly, answer frequently asked questions about the facilities available in the library and other services, and perform text mining that enables to render suggestions of sources or materials to the user when they are not aware of what specific source they are looking for. 

The bot is developed to have a chat with the user and extract the requests and hence respond to them accordingly. 

This bot is essentially a chat bot with the features of an EventBot. ?

Code drone vs documentation bot. ?

Tagline for the bot to encompass what the bot does. ?

## Use Cases 
#### Use Case 1: Issue a Book 
1. Preconditions 
   - A user "XYZ" has authenticated himself into the library system. [UC?]
2. Main Flow 
   - The user request to issue a specific book from the library [S1]
3. SubFlow 
   - The user specifies that they want to issue a book
   - The bot then responds by asking the user to specify which book they are interested in issuing 
   - The user then specifies the name of the book
   - The bot scours through the library catalogue for the name of the book and checks if it is available and returns the book if it is available [E1]
   - The bot then marks the book as "Issued" and hence makes it unavailable for being issued by anyone else until it has been returned. 
4. Alternate Flows
   - [E1] The bot is unable to locate the specified book in the library catalogue or the book has already been issued by another user and hence is available to be issued by the user,  the bot then replies to the user with the valid message stating that the book requested for is unavailable. 
        
#### Use Case 2: Return a Book 
1. Preconditions 
   - A user "XYZ" has authenticated himself into the library system. [UC?]
   - The user has issued a book from the library [Use Case 1]
2. Main Flow 
   - The user specifies that they want to return a book 
   - The bot then responds by asking for the name of the book to be returned and its Book_ID [E2]
   - The bot then locates the ID of the book and then resets the Issuer name, the status of the availablility of the book
   - The 
#### Answer simple questions instantly
#### Pattern matching and suggesting books from a set of queries posed by the user 
## Design Sketches 
## Architecture Design 


