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
```
1 Preconditions: User must have LIBRA Access Token in the System. User must know the type of dataset for which he wants suggestion. <!--User must have a data set to know about the library to be used.-->
2 Main Flow: 
  User requests library/API call suggestion for a dataset/image. Bot provides the best suitable library/API call to be used for the       selected dataset.
3 Sub Flow 1:
  [s1] User requests for Library/API call suggestion.
  [s2] Bot asks whether it is image or numerical dataset.
  [s3] User responds by selecting image dataset.
  [s4] Bot asks whether it is for phone or PC/Server.
  [s5] User responds by selecting his preference.
  [s6] Bot suggests the best library/API call to be used for the given User's preferences.
4 Sub Flow 2: 
  [s1] User requests for Library/API call suggestion.
  [s2] Bot asks whether it is image or numerical dataset.
  [s3] User responds by selecting numerical dataset.
  [s4] Bot asks to provide the dataset to be used for the Library/API call Suggestion.
  [s5] User uploads the dataset.
  [s6] Bot suggests the best library/API call to be used for the uploaded dataset.
5 Alternate Flow 1:
  [E1] User's dataset is neither image or numerical. Bot responds by giving some generic suggestion.
```

#### Use Case 2: Know about a Library/API call <!--Bot renders description for library/API call-->
```
1 Preconditions: User must have LIBRA Access Token in the System.
2 Main Flow: 
  User requests information about a Library/API call. Bot provides the information about the library/API call and the relevant links.
3 Sub Flow:
  [s1] User requests information about a Library/API call.
  [s2] Bot lists the Machine Learning Libraries in python asking User to select a Library.
  [s3] User selects the Library.
  [s4] Bot provides information about the selected Library and relevant links to it and asks User whether he wants a specific        information about a method/function.
  [s5] User responds by selecting his preference and enters the name of the method/function.
  [s6] Bot gives description and relevant links about the given method/function.
4 Alternate Flow:
  [E1] No known method/function is provided by the user. Bot gives a message that method/function is not found.
```
 
#### Use Case 3: Have a Question?<!--User posts a question in event of there existing no other similar question-->
```
1 Preconditions: User must have LIBRA Access Token in the System
2 Main Flow:
  User requests for the Q/A section and Bot directs User to the Q/A section for the selected Library.
3 Sub Flow:
  [s1] User requests the Q/A section from the Welcome message.
  [s2] Bot lists the Machine Learning Libraries in python asking User to select a Library.
  [s3] User selects the Library.
  [s4] Bot asks whether the User is looking for an answer or wants to post an answer.
  [s5] User selects that he is looking for an answer. 
  [s6] Bot asks whether the question is related to a specific function or is general.
  [s7] User enters an input according to his preference.
  [s8] Bot presents the pool of questions those match with User's preference.
  [s9] User selects a question to see the answer.
  [s10] Bot displays the answer and asks to post a question if the user doesn't find the answer helpful. 
  [s11] User proceeds to type the question.
4 Alternate Flow:
  [E1] User finds the question but there is no answer available.
  [E2] User finds the answer helpful and does not post the question.
  
```
 
#### Use Case 4: User posts an answer to an already existing question 
```
1 Preconditions: User must have LIBRA Access Token in System
2 Main Flow:  User wants to answer a question. Bot lists the questions for the user and option to answer them.
3 Sub Flow 1:
  [s1] User requests the Q/A section from the Welcome message.
  [s2] Bot lists the Machine Learning Libraries in python asking User to select a Library.
  [s3] User selects the Library.
  [s4] Bot asks whether the User is looking for an answer or wants to post an answer.
  [s5] User selects that he wants to post an answer.
  [s6] Bot asks whether the user wants to answer related to a specific function or is general.
  [s7] User enters an input according to his preference.
  [s8] Bot presents the unanswered pool of questions those match with User's preference.
  [s9] User selects a question and enters the answer.
  [s10] Bot asks if the question is not available then post both the question and answer.
  [s11] User enters both the question and answer.
4 Alternate Flow:
  [E1] User may not have answer for the listed Questions.
```
 
<!--#### Use Case 5: User posts an answer to a question posted by the user itself 
1 Preconditions:
2 Main Flow:
3 Sub Flow:
4 Alternate Flow:-->
 
## Design Sketches 
## Architecture Design 


