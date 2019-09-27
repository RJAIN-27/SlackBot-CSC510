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
#### Use Case 1: Library/API call Suggestion for a dataset <!-- Bot suggests the library/API call to be used, in answer to a user's question -->
```bash
1 Preconditions: User must have LIBBRA Access Token in System<!--User must have a data set to know about the library to be used.-->
2 Main Flow: 
  User requests library/API call suggestion by uploading the dataset. Bot provides the best library/API call to be used for the uploaded   dataset.
3 Sub Flow 1:
  [s1] User requests for Library/API call Suggestion for a dataset.
  [s2] Bot asks whether it is image or numerical dataset.
  [s3] User responds by selecting image dataset.
  [s4] Bot asks whether it is for phone or Workstation.
  [s5] User responds by selecting his preference.
  [s6] Bot provides the best library/API call to be used for the given User's preferences.
4 Alternate Flow 1:
  [E1] Dataset is not provided by the User.  
5 Sub Flow 2: 
  [s1] User requests for Library/API call Suggestion for a dataset.
  [s2] Bot asks whether it is image or numerical dataset.
  [s3] User responds by selecting numerical dataset.
  [s4] Bot asks for the dataset to be used for the Library/API call Suggestion.
  [s5] User uploads the dataset.
  [s6] Bot provides the best library/API call to be used for the uploaded dataset.
6 Alternate Flow 2:
  [E1] Dataset is not provided by the User.
```

#### Use Case 2: Know about a Library/API call <!--Bot renders description for library/API call-->
```bash
1 Preconditions: User must have LIBBRA Access Token in System
2 Main Flow: 
  User requests information about a Library/API call. Bot provides the information about the library/API call and the relevant links.
3 Sub Flow:
  [s1] User requests information about a Library/API call.
  [s2] Bot asks the User to enter the name of Library/API call
  [s3] User enters the name of the Library/API call.
  [s4] Bot provides information about the given Library/API call and relevant links to it.
4 Alternate Flow:
  [E1] No known library/API call is provided by the user.
```
 
#### Use Case 3: Have a Question?<!--User posts a question in event of there existing no other similar question-->
```bash
1 Preconditions: User must have LIBBRA Access Token in System
2 Main Flow:
  User searches for a question. Bot lists the existing Questions matching with User's Question. Bot lets User to post a question incase   User don't find relevant Questions.
3 Sub Flow:
  [s1] User selects Have a Question? Option from the bot's welcome message.
  [s2] Bot asks the Category of the Question. 
  [s3] User enters the Category of the Question.
  [s4] Bot asks User to enter the Question.
  [s5] User enters the Question.
  [s6] Bot displays Questions and their answers matching with User's Question and asks User to post Question if he didn't find the              answers helpful.
  [s7] User selects Post.
  [s8] Bot asks User to enter the Question by providing all the context.
  [s9] Bot posts the Question in the repository.
4 Alternate Flow:
  [E1] User finds the answers helpful.
```
 
#### Use Case 4: User posts an answer to an already existing question 
```bash
1 Preconditions: User must have LIBBRA Access Token in System
2 Main Flow:  User wants to answer a question. Bot lists the questions for the user and option to answer them.
3 Sub Flow 1:
  [s1] User selects Q/A option to go to the Question and Answer section.
  [s2] Bot asks the User about the Library name to list Questions and Answers related to that Library.
  [s3] User enters the Library name.
  [s4] Bot asks the User whether he is looking for an answer or he wants to post an answer.
  [s5] User selects post an answer.
  [s6] Bot provides the list of Questions.
  [s7] User selects a Question.
  [s8] Bot asks to share the Answer for that Question.
  [s9] User enters the Answer.
  [s10] Bot posts the Answer to the Question in repository. 
4 Alternate Flow:
  [E1] User may not have answer the listed Questions.
```
 
<!--#### Use Case 5: User posts an answer to a question posted by the user itself 
1 Preconditions:
2 Main Flow:
3 Sub Flow:
4 Alternate Flow:-->
 
## Design Sketches 
## Architecture Design 


