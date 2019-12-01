# Deployment 
The goal of this milestone is to demonstrate a fully deployed version of our Library Bot- L.I.B.R.A.
This slack bot is present in the slack workspace https://rajshreegroup.slack.com/ in the **Librarybot** channel. 
We have deployed the bot in the AWS environment using Ansible.

### Requirements 
On the local machine, for deployment, we will require A linux/UNIX/MAC machine, an Ubuntu Server and Python 2.7 and Ansible confugured in the system. 

## Deployment Scripts 
We have used the open source configuration management tool, Ansible, to provide and configure a remote environment for our Library Bot. 

The deployment scripts in Ansible are located in the folder [Deployment](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Deployment) in the repository. 
The deployment folder contains two Ansible playbooks
1. [setup.yaml](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Deployment/setup.yaml)
   - This playbook contains the setup and necessary installations for python, pip, git, nodejs, forever, npm, and other python packages required to run the code.
   - It also clones the git repository and runs the forever bot.
   
2. [requirement.yaml](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Deployment/requirements.yaml).<br/>
   - This playbook contains the python packages required to run the code.

### Steps to run deployment 
- In the inventory file we will have to give the public IP address of the AWS instance along with the other parameters and save the inventory file <br/>
Command: vim etc/ansible/hosts
- To run the deployment scripts we use the following command <br/>
Command: ansible-playbook setup.yaml -e file=requirements.yaml -v

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/first.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/requirements.png)

## Acceptance Tests 

TA User Account Credentials:

Pre-requisite Steps:
1. Login into the Slack channel with valid crendentials:
   - Channel Link -  https://app.slack.com/client/TPDPYLR63/CPDPYM023
   - Workspace - rajshreegroup.slack.com
   - Email-Id - librabot.testuser@gmail.com
   - User-Name - test_user
   - Password - Travel@123
2. Click on Librarybot channel

### UseCase1: Model Suggestion

**TestCase1:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to know the best model for this dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Class"

**Expected:**

Bot should give one or more model suggestions with a text file describing the process to arrive at best model for the given dataset.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_2.png)

**TestCase2:**
1. Test User selects a dataset [Crime.csv](https://drive.google.com/open?id=1XuUWbALxOR2t9NE4ErrF_olQuWJhgbJM) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to know the best model for this dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Category"

**Expected:**

Bot should give one or more model suggestions with a text file describing the process to arrive at best model for the given dataset. Bot should also identify this as categorical dataset and perform n-gram feature classication for each column and then train the dataset.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_3.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_4.png)

**TestCase3:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User types "I want to know the best model for this dataset." in the message field and presses 'Enter'
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "dummy" which is not present in the dataset.

**Expected:** 

The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_5.png)

**TestCase4:**
1. Test User doesn't upload a dataset.
2. Test User types "I want to know the best model for this dataset." in the message field and presses 'Enter'.

**Expected:**

Please upload the dataset along with your query.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_6.png)

**TestCase5:**
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User clicks upload button.

**Expected:**

I am sorry can you please give me a csv file with the details of what is to be done.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_7.png)

### UseCase2: Analyze the dataset.

**TestCase1:** 
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to analyze the dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "Class"

**Expected:**

Bot should give exploratory data analysis of the given dataset in txt format.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_8.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_9.png)

**TestCase2:** 
1. Test User selects a dataset [Wine.csv](https://drive.google.com/open?id=1DAMCOHTMpKuizsAS_SXApEmMgOhXJQ7x) to upload using the attachments button in the Librarybot channel.
2. Test User enters "I want to analyze the dataset." in the message field.
3. Test User clicks upload button.
4. Bot responds with a message "Please provide the target column"
5. Test User enters the target column "dummy" which is not present in the dataset.

**Expected:**

The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_10.png)

**TestCase3:**
1. Test User doesn't upload a dataset.
2. Test User types "I want to analyze the dataset." in the message field and presses 'Enter'

**Expected:**

Please upload the dataset along with your query.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_11.png)

**TestCase4:**
1. Test User selects a non csv file.
2. Test User clicks upload button.

**Expected:**

I am sorry can you please give me a csv file with the details of what is to be done

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_12.png)

### UseCase3: Know about Library/Functions Machine Learning.

**TestCase1:** 
1. Test User enters "I want to know about scikit library"

**Expected:**

1. Bot shows a brief description about scikit-learn library and the relevant links to find more information about the library.

2. In addition, Bot asks the following question: If you would like to have information about particular function in the above library, please enter the function name

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_13.png)

**TestCase2:(TestCase1 continuation)**

1. Test User enters "I would like to know about adaboostclassifier"

**Expected:**

Bot provides a brief description about adaboostclassifier function in the scikit-learn library.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_14.png)

**TestCase3:**

1. TestUser enters "I want to know about adaboostclassifier from scikitlearn library" 

**Expected:**

Bot provides a brief description about adaboostclassifier function in the scikit-learn library.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_15.png)

**TestCase4:**

1. Test User enters "I want to know about kires library"

**Expected:**

I am sorry, coudn't fetch the information. My team is working on making me better everyday by adding new functions and libraries in my database!

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_16.png)

**TestCase5:** 

1. Test User enters some random text "what is the height of eiffel tower?"

**Expected:**

Sorry, I didn't get you.

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_17.png)

**TestCase6:**
1. Test User enters "I want to know about scikit library"
2. Bot shows a brief description about scikit-learn library and the relevant links to find more information about the library. Bot asks if the Test User wants to know any specific function in the library.
3. Test User enters "I want to know about sin". (sin is not available in scikit library)

**Expected:**

I am sorry, coudn't fetch the information. My team is working on making me better everyday by adding new functions and libraries in my database!

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/uc1_18.png)

## Final Code

The final code for all 3 use cases can be found in the folder [code](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Code). 

This folder contains the folder [Datasets](https://github.ncsu.edu/csc510-fall2019/CSC510-23/tree/master/Code/Datasets) which contains the datasets that are used to test the functionality of the use cases. It also contains the database [libraryFile.xlsx](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/libraryFile.xlsx) that stores the information about the libraries and the functions for the third use case. 

**For Use Case 1** 

Description of code for Use case 1 
- Uses functions from [commonFunctions.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/commonFunctions.py) and reads the dataset as an input. 
- It splits this  into training set and testing set and performs model selection
- It writes the result into a file and returns this file 
- This code handles numerical and categorical data 
- It handles cases when the categories are a set of words or sentences, by performing n-gram extraction 
- The code for this use case can be found here 
  - [modelSelection.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelSelection.py)
  - [modelTraining.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelTraining.py)
  - [ngramTraining.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/ngramTraining.py)
- The unit test for this use case can be found here 
  - [modelSelTest.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/modelSelTest.py)
  
**For Use Case 2**

Description of code for Use case 2
- Uses functions from [commonFunctions.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/commonFunctions.py) and reads the dataset as an input. 
- It performs exploratory data analysis on the given data set (Correlation between variables, Normality tests and descriptive analystics) 
- It handles both numerical and categorical data 
- The code for this use case can be found here 
  - [analysis.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/analysis.py)
- The unit test for this use case can be found here
  - [analysis_unit_test.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/analysis_unit_test.py)

**For Use Case 3**

Description of code for Use case 3
- This code accepts the message from the user, tokenizes it and extracts the keywords through vectorization and 1-gram extraction.
- It then compares these keywords to the list of keywords in the [libraryFile.xlsx](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/libraryFile.xlsx) file. 
- If there is a match, it then returns the description against the respective keywords. 
- The code for this use case can be found here 
  - [KeywordExtraction.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/KeywordExtraction.py)
- The unit test for this use case can be found here 
  - [keywordExtTest.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/keywordExtTest.py)
  
**For mocking infrastructure** 

- The code for the mocking infrastructure can be found here 
  - [mocking_infrastructure.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/mocking_infrastructure.py)
- The json file for the mocking infrastructure can be found here 
  - [data.json](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/data.json)
  
**For connection with front end** 
- The code for connection with the front end to enable user interaction 
  - [command.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/command.py)
  - [bot.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/bot.py)
  - [event.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/event.py)
  - [slackbot.py](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Code/slackbot.py)
  
## Screencast Links
  
## Continuous Integration Service 

Continuous Integration is done using Jenkins which is hosted in the port 8080. Since we do not have complete user privileges for the repository, we do not have Webhooks. So, we are using Poll SCM to poll the repository every 15 minutes to check for any new commits. If any new commits are detected, then Jenkins makes a test build to check if all test cases are in compliance. 

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Jenkins1.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Jenkins2.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Jenkins3.png)
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/Jenkins4.png)



 

