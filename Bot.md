# BOT 

## Use Cases: 

### Use Case 1: Model Suggestion for a dataset <!-- Bot suggests the model to be used, in answer to a user's request about not having a clarity about what to do with the dataset --> <!-- User must have a dataset to know about the library to be used -->
```
1 Preconditions: User must have valid authorization to use the slack channel. User must provide a dataset for model suggestion.
2 Main Flow: 
  User provides a dataset and requests Model suggestion for the given dataset. Bot runs the Machine Learning techiniques(preprocessing, model building, model selection, etc.) in python on the dataset in the background and arrives at the best suitable model to be used for the dataset.
3 Sub Flow 1:
  [s1] User requests bot for model suggestion for a dataset and uploads the dataset.
  [s2] If the dataset is in .csv format, Bot asks user to give the target column.
  [s3] User gives the target column.
  [s4] Bot sends the dataset and target column to the backend where the a series of Machine Learning techiniques in Python are applied to find the best model for the dataset.
  [s5] The result from the procedure in [s4] is then passed back to the User.
4 Alternate FLow:
  [E1] User's dataset is not in .csv file. The bot responds by asking User to provide dataset with .csv format.
  [E2] The target variable specified by the user is not present in the dataset. 
```
##### Refinement in Use Case 1: 
The precondition for this use case has been changed from user requiring a LIBRA token to User needing a valid slack authorization. Another alternate flow has been added to account for the specified target variable not being present in the user's dataset. 

### Use Case 2: Data Analysis on a dataset <!-- Bot performs Exploratory Data Analysis (EDA) (includes statistical analysis) so that the user can understand the data before he/she can make any assumptions about it --> <!-- User must have a dataset to gain insights about the dataset -->
```
1 Preconditions: User must have valid authorization to use the slack channel. User must provide a dataset to gain insight.
2 Main Flow: 
  User provides a dataset and requests analysis on the given dataset. Bot performs the various statistical hypothesis tests and exploratory data analysis in python on the dataset in the background and returns the result to the user.
3 Sub Flow:
  [s1] User requests bot for data analysis on a dataset and uploads the dataset.
  [s2] If the dataset is in .csv format, Bot asks user to give the target column.
  [s3] User gives the target column.
  [s4] Bot performs series of statistical hypothesis tests and exporatory data analysis on the dataset in python at the backend.
  [s5] The results from the procedure in [s4] is then passed back to the User in form of .txt file.
4 Alternate FLow:
  [E1] User's dataset is not .csv file. The bot responds by asking User to provide dataset file of .csv format.
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
  [s3] Bot asks whether User wants to know about any specific method/function in the above Library/API.
  [s4] User responds by giving a name of the method/function he wants to explore.
  [s5] Bot gives description and relevant links about the given method/function.
4 Alternate Flow:
  [E1] No known library/function is provided by the user. Bot gives a message that library/function is not found.
```

##### Refinement in Use Case 3: 
The precondition for this use case has been changed from user requiring a LIBRA token to User needing a valid slack authorization. 


## Mocking Service Component 

The mocking program used for this milestone is [mocking_infrastructure.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/mocking_infrastructure.py) which mocks [KeywordExtraction.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/KeywordExtraction.py), [analysis.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/analysis.py) and [modelSelection.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelSelection.py). 

The program [test.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/test.py) is used to perform mock unittests for all the 3 usecases. The output is given here:
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/running_test_cases.png)

## Bot Implementation 

The code for the Bot Implementation and mock test is given [here](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Code)

The major files implementing the functionality of the three use cases are 

1. [modelSelection.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelSelection.py) 
2. [analysis.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/analysis.py) 
3. [KeywordExtraction.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/KeywordExtraction.py) 



## Selenium Testing 

The Selenium Testing files are given [here](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Selenium). 

1. Use Case 1 Happy Path:
    - Here we are uploading a csv file and specifying the target variable automatically and asserting if the output from the bot is as expected
2. Use Case 1 Sad Path: 
    - Here we are uploading the .csv file and specifying a target variable that is not present in the dataset, automatically, and we are asserting if the bot responds as expected by identifying that the target variable is not present in the dataset
3. Use Case 2 Happy Path: 
    - Here we are uploading a csv file and specifying the target variable automatically and asserting if the output from the bot is as expected
4. Use Case 2 Sad Path: 
    - Here we are uploading the .csv file and specifying a target variable that is not present in the dataset, automatically, and we are asserting if the bot responds as expected by identifying that the target variable is not present in the dataset
5. Use Case 3 Happy Path: 
    - Here we post a message with the keywords present in the library information database and we assert if the bot responds with the corresponding description of those keywords. 
6. Use Case 3 Sad Path: 
    - Here we post a message with the keywords that are not present in the library information database and we assert if the bot responds as expected with an appropriate error message. 

## Task Tracking 

## Screencast 
