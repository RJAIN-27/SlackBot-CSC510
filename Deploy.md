# Deployment Scripts 
Deployment scripts are located in the folder Deployment in the repository. The deployment folder contains two playbooks - [setup.yaml](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Deployment/setup.yaml) and  a vars_file - [requirement.yaml](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Deployment/requirements.yaml).<br/>

The playbook for setup contains tasks to download and install python, pip, git, nodejs, forever, npm, python packages required to run our code, git clone, run the bot forever. The playbook for requirement contains all the python packages required to run the code. 


# Acceptance Tests 

TA User Account Credentials:

Pre-requisite Steps:
1. Login to https://rajshreegroup.slack.com/ with valid crendentials
2. Click on Librarybot channel

### UseCase1: Model Suggestion

**TestCase1:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to know the best model for this dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Class"

Expected:

Bot should give one or more model suggestions with a text file describing the process to arrive at best model for the given dataset.

**TestCase2:**
1. Test User selects a dataset [Crime.csv](https://drive.google.com/open?id=1XuUWbALxOR2t9NE4ErrF_olQuWJhgbJM) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to know the best model for this dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Category"

Expected:

Bot should give one or more model suggestions with a text file describing the process to arrive at best model for the given dataset. Bot should also identify this as categorical dataset and perform n-gram feature classication for each column and then train the dataset.

**TestCase3:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to know the best model for this dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "dummy" which is not present in the dataset.

Expected: 

The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive.

**TestCase4:**
1. Test User doesn't upload a dataset.
2. Test User enters "I want to know the best model for this dataset." in the message field.

Expected:

Please upload the dataset along with your query.

**TestCase5:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User clicks upload button.

Expected:

I am sorry can you please give me a csv file with the details of what is to be done.

### UseCase2: Analyze the dataset.

**TestCase1:** 
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to analyze the dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Class"

Expected:

Bot should give exploratory data analysis of the given dataset in txt format.

**TestCase2:** 
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to analyze the dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "dummy" which is not present in the dataset.

Expected:

The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive.

TestCase3:
1. Test User doesn't upload a dataset.
2. Test User enters "I want to analyze the dataset." in the message field.

Expected:

Please upload the dataset along with your query.

TestCase4:
1. Test User selects a non csv file.
2. Test User clicks upload button.

Expected:

I am sorry can you please give me a csv file with the details of what is to be done

UseCase3: Know about Library/Functions Machine Learning.

TestCase1: 
1. Test User enters "I want to know about scikit library"

Expected:

1. Bot shows a brief description about scikit-learn library and the relevant links to find more information about the library.

2. In addition, Bot asks the following question: If you would like to have information about particular function in the above library, please enter the function name

TestCase2:(TestCase1 continuation)

1. Test User enters "I would like to know about adaboostclassifier"

Expected:

Bot provides a brief description about adaboostclassifier function in the scikit-learn library.

TestCase3:

1. TestUser enters "I want to know about adaboostclassifier from scikitlearn library" 

Expected:

Bot provides a brief description about adaboostclassifier function in the scikit-learn library.

TestCase4:

1. Test User enters "I want to know about kires library"

Expected:

I am sorry, we are still working and building our database!

TestCase5: 

1. Test User enters some random text "what is the height of eiffel tower?"

Expected:

Sorry, I didn't get you.

TestCase6:
1. Test User enters "I want to know about scikit library"
2. Bot shows a brief description about scikit-learn library and the relevant links to find more information about the library. Bot asks if the Test User wants to know any specific function in the library.
3. Test User enters "I want to know about sin". (sin is not available in scikit library)

Expected:




# Final Code 

