# BOT 

## Use Cases: 

### Use Case 1: Model Suggestion for a dataset <!-- Bot suggests the model to be used, in answer to a user's request about not having a clarity about what to do with the dataset --> <!-- User must have a dataset to know about the library to be used -->
```
1 Preconditions: User must have valid authorization to use the slack channel. User must provide a dataset for model suggestion.
2 Main Flow: 
  User provides a dataset and requests Model suggestion for the given dataset. Bot runs the Machine Learning techiniques(preprocessing, model building, model selection, etc.) in python on the dataset in the background and arrives at the best suitable model to be used for the dataset.
3 Sub Flow 1:
  [s1] User requests bot for model suggestion for a dataset.
  [s2] Bot asks User to upload a dataset for which he/she needs suggestion.
  [s3] User uploads the dataset.
  [s4] Bot sends the dataset to the backend where the type of dataset(Eg: Numeric or Alphanumeric) is determined and a series of Machine Learning techiniques in Python are applied to find the best model for the dataset.
  [s5] The result from the procedure in [s4] is then passed back to the User.
4 Alternate FLow:
  [E1] User's dataset is neither numerical nor alphanumeric. The bot responds by asking User to provide numeric or alphanumeric dataset.
  [E2] The target variable specified by the user is not present in the dataset. 
```
##### Refinement in Use Case 1: 
The precondition for this use case has been changed from user requiring a LIBRA token to User needing a valid slack authorization. Another alternate flow has been added to account for the specified target variable not being present in the user's dataset. 

### Use Case 2: Data Analysis on a dataset <!-- Bot performs Exploratory Data Analysis (EDA) and Statistical Hypothesis Tests so that the user can understand the data before he/she can make any assumptions about it --> <!-- User must have a dataset to gain insights about the dataset -->
```
1 Preconditions: User must have valid authorization to use the slack channel. User must provide a dataset to gain insight.
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
  [E2] The target variable specified by the user is not present in the dataset. 
```
##### Refinement in Use Case 2: 
The precondition for this use case has been changed from user requiring a LIBRA token to User needing a valid slack authorization. Another alternate flow has been added to account for the specified target variable not being present in the user's dataset. 

### Use Case 3: Know about a Library/API <!--Bot renders description for library/API that is requested by the user-->
```
1 Preconditions: User must have valid authorization to use the slack channel.
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

##### Refinement in Use Case 3: 
The precondition for this use case has been changed from user requiring a LIBRA token to User needing a valid slack authorization. 


## Mocking Service Component 

The mocking files used for this milestone are given "here". Our bot mocks all the calls to the API for all the use cases. 

## Bot Implementation 

The code for the Bot Implementation is given "here"

The major files implementing the functionality of the three use cases are 

1. KeywordExtraction.py 
2. Analysis.py 
3. ModelSelection.py 

## Selenium Testing 

The Selenium Testing files are given "here". "More description of test cases to be written". 

## Task Tracking 

## Screencast 
