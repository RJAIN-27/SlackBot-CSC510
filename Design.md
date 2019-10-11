# Design

## Objective 
To develop a bot system that assists software engineers/developers with their requests or queries pertaining to Machine Learning  libraries/APIs in Python and datasets.

## Problem Statement  
Machine Learning applications are flourishing in every field. With data becoming the new oil, it is important for any organization to use data to enhance their business. For this purpose, many organizations us Machine Learning APIs, the popular ones  being Scikit-Learn, TensorFlow, Keras, MxNet, from Python. But the process of Machine Learning and usage of these APIs are still unclear to many which makes it complex for users who are not experts, to use.

The information available online regarding the usage of such APIs and libraries is vast and diverse. It is tedious to scout around a multitude of these sources and nail down on a satisfying answer and proceed with the implementation. Therefore, it will certainly be beneficial to have a solution that will answer questions regarding these libraries and the implementation on datasets, posed by users of these APIs, in a concise and satisfying manner, all under the same roof, especially when the users are unclear about what has to be done with a dataset.  

## Bot Description

The situation presented in the previous section can be eased by introducing our bot system L.I.B.R.A. (Library-Intensive Bot for Resource Assistance) which helps the users in understanding the ML APIs of Python in a concise and systematic manner, by responding to the user’s requests. The bot is also primarily developed to aid the users in understanding the dataset, as well as what model has to be applied on the users' dataset, by applying a series of elegant machine learning techniques internally on the dataset. This way the users get the solution to their questions all under one roof.
 
**The bot is developed to handle the following operations** 

- The user wishes to understand what model to apply on a dataset. The bot interacts with the user to get the dataset. It then performs the standard machine learning techniques in python, on the dataset and suggests the best suited model for the same. This reduces the user's effort in trying to understand from a myriad of sources on what has to be done with the dataset. This feature is applicable when the users' data set is either a numerical one or a combination of numeric and alphanumeric content. 

- The user wishes to understand the dataset better. The bot interacts with the user to get the dataset. The bot then performs basic Exploratory Analysis on the dataset and yields the results to the user. It also performs various statistical tests like Normality Tests, Coefficient tests, Parametric Statistical Hypothesis Tests and Nonparametric Statistical Hypothesis Tests and give the results to the user.

- The user requests for information about an ML library or API in python, then bot renders this information. 

This bot is developed to respond to the user’s requests which act as events, which makes this a response bot. The bot follows the "reactor" design pattern which chats with the users when they ask their questions as well as respond to cases, but has no memory of who the user is.


## Use Cases 
#### Use Case 1: Model Suggestion for a dataset <!-- Bot suggests the model to be used, in answer to a user's request about not having a clarity about what to do with the dataset --> <!-- User must have a dataset to know about the library to be used -->
```
1 Preconditions: User must have LIBRA Access Token in the System. User must provide a dataset for suggestion.
2 Main Flow: 
  User provides a dataset and requests Model suggestion for the given dataset. Bot runs the Machine Learning techiniques(preprocessing, model building, model selection, etc.) in python on the dataset in the background and arrives at the best suitable model to be used for the dataset.
3 Sub Flow 1:
  [s1] User requests bot for model suggestion for a dataset.
  [s2] Bot asks User to upload a dataset for which he/she needs suggestion.
  [s3] User uploads the dataset.
  [s4] Bot analyses sends the dataset to the backend where the type of dataset(Eg: Numeric or Alphanumeric) is determined and a series of Machine Learning techiniques in Python are applied to find the best model for the dataset.
  [s5] The result from the procedure in [s4] is then passed back to the User.
4 Alternate FLow:
  [E1] User's dataset is neither numerical nor alphanumeric. The bot responds by asking User to provide numeric or alphanumeric dataset.
```

#### Use Case 2: Data Analysis on a dataset <!-- Bot performs Exploratory Data Analysis (EDA) and Statistical Hypothesis Tests so that the user can understand the data before he/she can make any assumptions about it --> <!-- User must have a dataset to gain insights about the dataset -->
```
1 Preconditions: User must have LIBRA Access Token in the System. User must provide a dataset to gain insight.
2 Main Flow: 
  User provides a dataset and requests analysis on the given dataset. Bot performs the various statistical hypothesis tests and exploratory data analysis in python on the dataset in the background and returns the result to the user.
3 Sub Flow:
  [s1] User requests bot for data analysis on the dataset.
  [s2] Bot asks User to upload a dataset for which he/she wants to perform analysis on.
  [s3] User uploads the dataset.
  [s4] Bot performs series of statistical hypothesis tests and exporatory data analysis on the dataset in python at the backend.
  [s5] The results from the procedure in [s4] is then passed back to the User.
4 Alternate FLow:
  [E1] User's dataset is neither numerical nor alphanumeric. The bot responds by asking User to provide numeric or alphanumeric dataset. 
```

#### Use Case 3: Know about a Library/API <!--Bot renders description for library/API that is requested by the user-->
```
1 Preconditions: User must have LIBRA Access Token in the System.
2 Main Flow: 
  User requests information about a Library/API. Bot provides the information about the library/API and the relevant links.
3 Sub Flow:
  [s1] User asks a question about particular Library/API. (Eg: "Hey, I want to know about Scikit Learn Library")
  [s2] Bot answers User's question with information about the Library/API and provides relevant links.
  [s4] Bot asks whether User wants to know about any specific method/function in the above Library/API.
  [s5] User responds by giving a name of the method/function he wants to explore.
  [s6] Bot gives description and relevant links about the given method/function.
4 Alternate Flow:
  [E1] No known method/function is provided by the user. Bot gives a message that method/function is not found.
```
 
 
## Design Sketches

### Wireframe

**Case 1: When user would like to choose best model for a dataset**

The bot takes the csv file and sends it to the server where a python program is executed with the file to determine the best model by preprocessing and normalization, complex preprocessing like factoring, n-gram keywork extraction etc.

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire1.png" height="540" width="350"> 
</p>

***Alternate flow:***

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire1a.png" height="540" width="350"> 
</p>

**Case 2: When user would like to analyze a dataset:**

The bot takes the csv file and sends it to the server where a python program is executed with the file to perform various statistical tests and exploratory data analysis.

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire2.png" height="540" width="350"> 
</p>

***Alternate flow:***

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire2a.png" height="540" width="350"> 
</p>

**Case 3: When the user wants to know about a library or function:**

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire3.png" height="540" width="350"> 
</p>

**If bot doesn't understand the user's query/request:**

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire4.png" height="540" width="350">
</p>

**User feedback: The bot asks user's feedback regarding the task it performed and also asks if the user would like to perform any other tasks:**

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire5.png" height="540" width="350"> <img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/wireframes/wire6.png" height="540" width="350">
</p>

### Story board
#### Case 1: When user would like to choose best model for a dataset

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1.png">
</p>

##### Alternate flow if the dataset is not in .csv format:

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_1a.png">
</p>

#### Case 2: When user would like to analyze a dataset

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_2.png">
</p>

##### Alternate flow if the dataset is not in .csv format:

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_2a.png">
</p>

#### Case 3: When the user wants to know about a library or function

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_3.png">
</p>

#### If bot doesn't understand the user's query/request:

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_4.png">
</p>

#### User feedback: The bot asks user's feedback regarding the task it performed and also asks if the user would like to perform any other tasks

<p align="center">
<img src="https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/storyboard/sb_c_5.png">
</p>

## Architecture Design 

### Architecture Diagram and component details:

**The architecture diagram:**
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/Architecture%20Diagram%20new.png)

The architecture consists of three major components:-
1. Mattermost bot as a client for interacting with the user.
2. Server which processes the client request by calling appropriate Python APIs’.
3. A database required to store information regarding the description for Machine Learning APIs in Python

Within these 3 main components the function of the sub components are as follows: 

**1. Front end of the bot**

   *- Suggest an ML model for a given dataset:*
   
     - The user specifies that they wish to know what the best model is to apply on their dataset(numerical/image). The bot passes this request to the Extraction Component which then understands the intent of the user and passes the intent and the corresponding entities to the ML Component. In the ML Component a series of Machine Learning techniques are applied to arrive at the best model for a dataset. This result is passed to the Message Generator which then passes the appropriate messages. 
   
   *- User wants to understand the dataset:*
   
      - The user specifies that they wish to understand a dataset(numerical/alphanumeric). The bot passes this request to the Extraction Component which then understands the intent of the user and passes the intent and the corresponding entities to the ML Component. The ML component performs basic Exploratory Analysis on the dataset and yields the results to the Message Generator. It also performs various statistical tests like Normality Tests, Coefficient tests, Parametric Statistical Hypothesis Tests and Nonparametric Statistical Hypothesis Tests and give the results to the Message Generator. The Message Generator passes the appropriate messages to the user.
   *- Look for a description of a Library/API:*
   
      - The user requests for information about an ML library or API in python. This request is extracted by the extraction component and then sent to the message generator which fetches the relevant information from the ML Library/API Information database and delivers the result back to the user 
   
**2. Backend of the bot**

   *- Extraction component:*
      
      - This extracts the users’ intent and the corresponding inputs (entities) from the user and passes it on to the other components accordingly 
   
   *- Message Generator:*
   
      - This component has a set of predefined questions which are asked to the user in order to extract the intent of the user. It also responds to the users’ requests with the content it receives from the respective components responsible for handling the users' request. 
  
  *- ML Component:*
      
      - This component accepts the numerical/alphanumeric data set, and applies a set of ML techniques to analyse the data set and perform model selection. This result is passed to the Message Generator.

**3. Database**
   
   *- ML Library/API Information Bank:*
      
      - This consists of the various libraries and functions available and their corresponding descriptions.

### Architecture constraints and guidelines:
The following are the constraints of the bot:-
1. For the first two case, when the user wishes to understand what model to apply on a dataset, the bot can only suggest models for a numerical data set and alphanumerical dataset. That is, the dataset type is restricted to only numerical and alphanumeric. 
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
