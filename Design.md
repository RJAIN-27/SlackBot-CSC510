# Design

## Objective 
To develop a bot system that assists software engineers/developers with their requests or queries pertaining to Machine Learning  libraries/APIs in Python.

## Problem Statement  
Machine Learning APIs are flourishing in the developer world, and the web is becoming a mashup of interconnected APIs, the popular ones in Python being Scikit-Learn, TensorFlow, Keras, MxNet. But the usage of these APIs are still unclear to many, which makes it complex for users who are not experts, to use. 

The information available online regarding the usage of such APIs and libraries is vast and diverse. It is tedious to scout around a multitude of these sources and nail down on a satisfying answer and proceed with the implementation. Therefore, it will certainly be beneficial to have a solution that will answer questions posed by users of these APIs in a concise and satisfying manner, all under the same roof.  

## Bot Description

The situation presented in the previous section can be eased by introducing our bot system L.I.B.R.A. (Library-Intensive Bot for Resource Assistance) which helps the users in understanding the ML APIs of Python in a concise and systematic manner, by responding to the user’s requests. This way the users get the solution to their questions all under one roof.
 
The bot is developed to handle four cases. First case is when the user wishes to understand what model to apply on a dataset , the bot interacts with the user to understand what the dataset is and where it is to be deployed, and then suggests the appropriate model to fit on the data set. The second case is when the user requests for information about an ML library or API in python, then bot renders this information. Third case is when the user wishes to look for an answer to a question. If there is no existing answer for the question then the user simply posts the question. The fourth case is when the user posts an answer to an already existing question. If no such question exists then the user posts an answer to a question that is also posted by the same user. This makes it a Documentation Bot as it is equipped to answer users' questions. This bot is developed to respond to the user’s requests which act as events, which makes this a response bot. The bot follows the "reactor" design pattern which chats with the users when they ask their questions as well as respond to cases, but has no memory of who the user is.


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
 
#### Use Case 4: Post an answer 
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

### Wireframe

**Case 1: When user would like to choose best library or model depending upon the dataset and deployment environment**

*Case 1a: When user would like to choose best library for image dataset:*

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire1.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire2.png" height="540" width="350">

*Case 1B: When user would like to choose best model for numerical dataset:*

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire3.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire4.png" height="540" width="350">

*Case 1C: When user has dataset which is neither image dataset nor numerical dataset:*

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire5.png" height="540" width="350">

**Case 2: When the user wants to know about a library or function:**

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire6.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire7.png" height="540" width="350">

**Case 3: When user wants to search for an answer to the question. If the question is not available, the user can post the question:**

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire8.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire9.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire10.png" height="540" width="350">

**Case 4: When user wants to answer an asked question. If the question is not present, the user can post both question and answer:**

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire11.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire12.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire13.png" height="540" width="350">

**User feedback: The bot asks user's feedback regarding the task it performed and also asks if the user would like to perform any other tasks:**

<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire14.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire15.png" height="540" width="350">


### Story board
#### Case 1: When user would like to choose best library or model depending upon the dataset and deployment environment

##### Case 1a: When user would like to choose best library for image dataset

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1_1_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1_1_2.png)

##### Case 1b: When user would like to choose best model for Numerical dataset

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1_2_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1_2_2.png)

##### Case 1c: When user has dataset which is none of the above

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1_3.png)

#### Case 2: When the user wants to know about a library or function

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_2_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_2_2.png)

#### Case 3: When user wants to search for an answer to the question. If the question is not available, the user can post the question

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_3_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_3_2.png)

#### Case 4: When user wants to answer an asked question. If the question is not present, the user can post both question and answer

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_4_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_4_2.png)

#### User feedback: The bot asks user's feedback regarding the task it performed and also asks if the user would like to perform any other tasks

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_5.png)


## Architecture Design 

### Architecture Diagram and component details:

**The architecture diagram:**
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/Architecture%20Diagram.png)

The architecture consists of three major components:-
1. Mattermost bot as a client for interacting with the user.
2. Server which process the client request by calling appropriate Python APIs’.
3. A datastore required for storing commonly asked questions and their corresponding answers and a datastore required to store information regarding the description for Machine Learning APIs in Python

Within these 3 main components the function of the sub components are as follows: 

**1. Front end of the bot**

   *- Suggest an ML model for a given dataset:*
   
     - The user specifies that they wish to know what the best model is to apply on their dataset(numerical/image). The bot passes this request to the Extraction Component which then understands the intent of the user and passes the intent and the corresponding entities to the respective components, i.e. Message Generator for image data set, and Model Suggestion Component for numerical data set. The result is then passed back to the user through the Message Generator component.  
   
   *- Look for a description of a Library/API:*
   
      - The user requests for information about an ML library or API in python. This request is extracted by the extraction component and then sent to the message generator which fetches the relevant information from the ML Library/API Information database and delivers the result back to the user 
   
   *- Look for an answer:* 
      
      - The user posts a question to the bot which is extracted by the extraction component which then sends it to the message generator in turn. The message generator then looks into the Q/A Bank for then answer to the question and returns it to the user, if there exists some answer, and an appropriate message in the case that there is no answer to the user’s question. 
   *- Post an answer:*
      
      - The extraction component extracts the user’s intent to post an answer for a question and passes it to the message generator which then looks into the Q/A bank for the question and then allows the user to post an answer to the question and then write the answer back to the Q/A database. 

**2. Backend of the bot**

   *- Extraction component:*
      
      - This extracts the users’ intent and the corresponding inputs (entities) from the user and passes it on to the other components accordingly 
    - Message Generator: 
      - This component has a set of predefined questions which are asked to the user in order to extract the intent of the user. It also responds to the users’ requests with the content it receives from the respective components responsible for handling the request. 
   *- Model Suggestion:*
      
      - This component accepts the numerical data set, preprocesses it, applies a set of models from the scikitlearn package in Python and arrives at the best model for the dataset and passes on this as the result back to the user via the message generator.

**3. Databases**
   
   *- Q/A Bank:*
      
      - This consists of a set of commonly asked questions and answers related to ML libraries in Python 
   *- ML Library/API Information Bank:*
      
      - This consists of the various libraries available and their corresponding descriptions.

### Architecture constraints and guidelines:
The following are the constraints of the bot:-
1. For the first case, when the user wishes to understand what model to apply on a dataset, the bot can only suggest models for image or a numerical data set. 
2. The bot has limited number of functionality and focuses only on machine learning APIs and is equipped to handle only the use cases specified.
3. Since the bot follows a reactor design pattern, the user cannot follow up on any of the operations.  

### Additional design patterns:
The following are the design patterns that are to be implemented in the project.
1. ***Builder Pattern-*** This bot separates object construction from its representation and hence follows the builder pattern
2. ***Object-Pool Pattern -*** This bot is developed to avoid expensive acquisition and release of resources by recycling objects that are no longer in use 
3. ***Bridge Pattern-*** It is required for the clients of this bot to not be exposed to the complexity of the implementation of the objects. Therefore, this bot follows the bridge pattern which separates an object’s interface from its implementation
4. ***Chain-of-responsibilty Pattern -*** There is no direct coupling between the sender of a request (the user) and the receiver (the destination of the user’s intent). The user’s request passes through a set of processing elements instead and hence this bot follows the chain-of-responsibilty pattern.
5. ***Mediator Design Pattern-*** This pattern eases the communication between different objects by defining an object that encapsulates how a set of objects interact. For this bot, there is a component that promotes loose coupling by keeping objects from referring to each other explicitly
6. ***Factory Pattern -*** To create an instance of several derived classes, this pattern is followed. This facilitates easy management, instantiation and delegation of objects and other creation details supplied by the client.
7. ***Conversational-styled pattern -*** the interaction between the user and the bot will follow typical query-response pattern.
8. ***Command -*** To encapsulate the tasks to be performed as objects and passing them on for further execution through other components, this pattern is followed.
