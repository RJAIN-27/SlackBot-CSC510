# Initial Draft 

## Objective 
To develop a bot system that assists visitors with their requests and queries pertaining to the library. 
## Problem Statement  
Consider a library "ABC" which hosts several books and scholarly articles that can be accessed physically and digitally. The library also has several visitors, but has only a handful of librarians to attend to the visitors. This results in a huge load on the librarians especially during peak and late hours which might increase the wait time for the visitors as well. 

There are also some cases when the visitors are not definitive of what sources they are looking for. In such cases, it becomes difficult for a librarian to manually search and suggest what might be a potential source.

## Bot Description

This situation presented in the previous section can be eased by introducing a bot system that interacts with the vistors and caters to their interests in the same way that a librarian does, in other words has a chat with the visitors to understand their requests. Having a bot system to chat with at any hour of the day without having to wait for the librarian also might be an optimal solution for the visitors. Adding the feature of being able to understand the visitor's query and suggesting a list of sources that the visitor might find useful is a bonus to using a bot system for library management.  

The bot is developed to handle issuing books to visitors, accepting returned books, answering simple queries regarding facilities and services offered by the library, and additionally suggesting top 5 sources that closely match a query posed by the visitor on what kind of source they are looking for, by performing text mining on such a query. This also makes it a Documentation bot as it is equipped to answer users in a human-like manner. Therefore, this is a reactor bot which is designed to both, chat with the users as well as respond to events.

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


