# Initial Draft 

## Objective 
To develop a bot system that assists software engineers/developers with their requests or queries pertaining to Machine Learning  libraries/APIs in Python.

## Problem Statement  
Machine Learning APIs are flourishing in the developer world, and the web is becoming a mashup of interconnected APIs, the popular ones in Python being Scikit-Learn, TensorFlow, Keras, MxNet. But the usage of these APIs are still unclear to many, which makes it complex for users who are not experts, to use. 

The information available online regarding the usage of such APIs and libraries is vast and diverse. It is tedious to scout around a multitude of these sources and nail down on a satisfying answer and proceed with the implementation. Therefore, it will certainly be beneficial to have a solution that will answer questions posed by users of these APIs in a concise and satisfying manner, all under the same roof.  

## Bot Description

The situation presented in the previous section can be eased by introducing our bot system L.I.B.R.A. (Library-Intensive Bot for Resource Assistance) which helps the users in understanding the ML APIs of Python in a concise and systematic manner, the same way a human expert would help. In other words, it chats with the user to understand what the request of the user is, and then responds to it by yielding information about the keywords related to the APIs and corresponding libraries, and also answer the questions in a human-like manner. This way the users get the solution to their questions all under one roof.
 
The bot is developed to handle four cases. First, when the user wishes to search for description of a library/function, the user sends a query request to the bot with the question, the bot responds by giving information about the libraries, API or functions related to keywords in the query. The second case is when the user wishes to only post a question when there exists no similar question and thereby no definite answer. The third case is when the user wishes to post an answer to an existing question.The fourth case is when the user wishes to post an answer to a question posted by the user itself. This makes it a Documentation Bot as it is equipped to answer users' questions in a human-like manner. This bot follows the "reactor" design pattern which chats with the users when they ask their questions as well as responds to cases, but has no memory of who the user is.

## Use Cases 
#### Use Case 1: Library/API call Suggestion <!-- Bot suggests the library/API call to be used, in answer to a user's question -->
```bash
1 Preconditions: User must have LIBBRA Access Token in System<!--User must have a data set to know about the library to be used.-->
2 Main Flow: 
  User requests library/API call suggestion by uploading the dataset. Bot provides the best library/API call to be used for the uploaded   dataset.
3 Sub Flow:
  [s1] User requests for Library/API call Suggestion.
  [s2] Bot asks for the dataset to be used for the Library/API call Suggestion.
  [s3] User uploads the dataset.
  [s4] Bot provides the best library/API call to be used for the uploaded dataset.
4 Alternate Flow:
  [E1] Dataset is not provided by the User.
```

#### Use Case 2: Bot renders description for library/API call
```bash
1 Preconditions: User must have LIBBRA Access Token in System
2 Main Flow: 
  User requests information about a library/API call. Bot provides the information about the library/API call and the relevant links.
3 Sub Flow:
  [s1] User requests information about a particular library/API call.
  [s2] Bot provides the information about the library/API call and the relevant links.
4 Alternate Flow:
  [E1] No known library/API call is provided by the user.
```
 
#### Use Case 3: User posts a question in event of there existing no other similar question 
```bash
1 Preconditions:
2 Main Flow:
3 Sub Flow:
  [s1] 
  [s2]
  [s3]
  [s4]
4 Alternate Flow:
```
 
#### Use Case 4: User posts an answer to an already existing question 
```bash
1 Preconditions:
2 Main Flow:
3 Sub Flow:
  [s1] 
  [s2]
  [s3]
  [s4]
4 Alternate Flow:
```
 
<!--#### Use Case 5: User posts an answer to a question posted by the user itself 
1 Preconditions:
2 Main Flow:
3 Sub Flow:
4 Alternate Flow:-->
 
## Design Sketches 
## Architecture Design 


