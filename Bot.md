# BOT 

The library bot L.I.B.R.A. is developed in Slack Environment.

## Bot Implementation 

The code for the Bot Implementation and mock unittest is given [here](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Code)

## Use Cases Refinement: 

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
##### Future Implementation 
We will develop the use case to preprocess the input and support categorical datasets as well, and also normalize the dataset depending on the normality of the dataset. 

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

##### Future Implementation 
We will develop the use case to process the data for statistical tests as well. 

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

##### Future Implementation 
We will increase the size of the database and develop the use case to also provide information about specific methods or functions in a given Library/API. 


## Mocking infrastructure

The programs are written in python.

The mocking program used for this milestone is [mocking_infrastructure.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/mocking_infrastructure.py) which mocks the basic log [KeywordExtraction.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/KeywordExtraction.py), [analysis.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/analysis.py) and [modelSelection.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelSelection.py). 

The program [mocking_infrastructure.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/mocking_infrastructure.py) also mocks the REST API calls i.e., instead of fetching the json file from the server, using python Mock function, the get() API call is mocked with locally present json file which is used to fetch details and paths.

To run the bot, the user is required to install mock package and openpyxl package.

` pip install mock `

` pip install openpyxl `


## Mock Unit testing

The mock unittest of the program is given [here](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/test.py). This program performs 6 unittests (2 for each usecase).

To run the unittest : `python test.py`

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/running_test_cases.png)

## Selenium testing of each use case 

The Selenium Testing files are given [here](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Selenium). 

1. **Use Case 1 Happy Path:**
    - We are uploading a csv file and specifying the target variable automatically and asserting if the output from the bot is as expected([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase1HappyPath.java))
2. **Use Case 1 Alternate Path:**
    - We are uploading the .csv file and specifying a target variable that is not present in the dataset, automatically, and we are asserting if the bot responds as expected by identifying that the target variable is not present in the dataset ([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase1AltFlow.java))
3. **Use Case 2 Happy Path:**
    - We are uploading a csv file and specifying the target variable automatically and asserting if the output from the bot is as expected([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase2HappyPath.java))
4. **Use Case 2 Alternate Path:**
    - We are uploading the .csv file and specifying a target variable that is not present in the dataset, automatically, and we are asserting if the bot responds as expected by identifying that the target variable is not present in the dataset([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase2AltFlow.java))
5. **Use Case 3 Happy Path:**
    - We post a message with the keywords present in the library information database and we assert if the bot responds with the corresponding description of those keywords. ([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase3HappyPath.java))
6. **Use Case 3 Alternate Path:**
    - We post a message with the keywords that are not present in the library information database and we assert if the bot responds as expected with an appropriate error message.([code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Selenium/src/UseCase3AltFlow.java))

## Screencast 
Screencast video of demonstration of use cases using Selenium testing given [here](https://drive.google.com/file/d/10fMjVP0apT3TCHHXmkwVSOpa8-kdXrMB/view?usp=sharing)

## Assumptions and Constraints 
#### System and Execution 
1. We have developed the backend to work for Python 2 
#### Use Cases 
1. **Use case 1**: For this milestone we have developed the first use case to handle only numerical datasets 
2. **Use case 2**: For this milestone we have developed the use case to perform simple exploratory data analytics 
3. **Use case 3**: For this milestone we are using a small database with limited number of keywords, to store the description 
#### Testing 
1. For use cases 1 and 2 we are using a sample CSV file called Wine.csv
2. For use case 3 we are using a small database with limited keywords to compare with the keywords given in the user's message

