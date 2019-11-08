# PROCESS 

### Iteration 1 (Wed Oct 23-- Fri Nov 1):

**Division of Tasks using kanban board:**
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/kanban1.jpg)

### Meeting Notes (Thu Oct 24th 2019)

**Key Decisions:**
  - Decided on final use case flow for each of the three use cases.
  - Divided the development of the use cases into two iterations and assigned tasks/stories(in the above kanban board) for the development of the use cases under the first iteration.
  - Assigned the stories to each of the 4 team members and set deadlines to complete the story development.

**Attendees:**
- Sandeep Kundala 
- Nita Radhakrishnan 
- Rajshree Jain 
- Manikanta NVSR 

  
### Meeting Notes (Thu Oct 28th 2019)
**Key Decisions:**
  - Had a discussion about the progress of tasks/stories.
  - Discussed about the difficulties in developing the tasks and helped each other in resolving the issues.

**Attendees:**
- Sandeep Kundala 
- Nita Radhakrishnan 
- Rajshree Jain 
- Manikanta NVSR 

#### Use Case 1: Selecting best model for the dataset
**Task 1:** Program to accept the csv file and check whether target column is present (2)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Start Date:** 23rd October 2019
- **End Date:** 24th October 2019
- **Blockers:** None
- **Comment**:
    * Used Python Pandas module to read the CSV file and check the columns.

**Task 2:** Train the dataset using different ML Algorithms and choose the best model (8)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Start Date:** 25th October 2019
- **End Date:** 27th October 2019
- **Blockers:** XGBoost Classifier Installation - Incompatible with PyCharm
- **Comment:**
     - Preprocess the dataset and split the dataset into training and testing dataset.
     - Used SciKit library to train the models.
     - XGBoost Classifier - The support to XGBoost Classifier is not present in PyCharm. Tested the code using terminal window (command prompt)

#### Use Case 2: Performing Exploratory Data Analysis on user data set 
**Task 1:** Read the user’s .csv file and generate .txt file to write results of EDA into it (2)
- **Assigned:** Nita Radhakrishnan (@nradhak2)
- **Status:** Completed 
- **Blockers**: None 
- **Comment**: 
     - Read the user’s .csv file using pandas library 
     - Generated dynamic text files based on date and time, to write results of exploratory analysis into, and returned the file to user 

**Task 2:** Perform descriptive exploratory data analysis on the user's dataset and write the contents of the result obtained from the analysis into a file  (8)
- **Assigned:** Nita Radhakrishnan (@nradhak2)
- **Status**: Completed
- **Blockers**: None 
- **Comment**:
    - Described the data set on basis of target variable and provided summary statistics
    - Calculated descriptive statistics for data set 
    - Calculated correlation values between variables in dataset using 3 different methods
    - Tested Normality of data using 3 different tests  

#### Use Case 3: To provide user with description of user-requested Library/API and corresponding functions 
**Task 1:** Develop the database CSV File which includes ML Libraries and Functions in Python
- **Assigned:** Manikanta (@vnukala2)
- **Status:** Completed
- **Blockers:** None 
- **Comment**:
    - Added some popular libraries in Python related to Machine Learning such as Numpy, Keras, PyTorch and their relevant links.
    
**Task 2:** Develop the working service of the retrieval of information about Libraries and Functions.(5)
- **Assigned:** Manikanta (@vnukala2)
- **Status:** Completed
- **Blockers:** None 
- **Comments**:
    - Developed the working service of the retrieval using keyword extraction and sending the database information to the bot.

#### Integration 
**Task 1:** Intelligently select which use case to execute depending upon user's message.(4)
- **Assigned:** Rajshree (rjain27)
- **Status:** Completed
- **Blockers:** None 
- **Comments:** 

**Task 2:** Determine all the use cases and check how the bot should handle the requests and responses in all the cases.(6)
- **Assigned:** Rajshree (rjan27)
- **Status:** Completed
- **Blockers:** None 
- **Comments:** 

**Practices**:  
  - We followed pair programming while developing the tasks. For example, Task 2 in Usecase 3 is implemented by @vnukala2 while @nradhak2 guides the steps.
  - We followed Continuous Integration and Continuous Developement while developing the tasks. For example, Everytime a task is completed we did an end to end testing for that task and resolved any integration issues occurred.

### Iteration 2 (Sat Nov 2--Fri Nov 8th):

#### Use Case 1: Selecting best model for the dataset

**Task 1:** Log the tasks performed by the bot in the backend and give it to the user for reference (1)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Start Date:** 2nd November 2019
- **End Date:** 3rd November 2019
- **Blockers:** None
- **Comment:** File handling operation - all the logs are saved in file *modelSelectionProcess.txt*

**Task 2:** Factorize and update the dataset if Categorical column is present (3)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Start Date:** 2nd November 2019
- **End Date:** 3rd November 2019
- **Blockers:** None
- **Comment:** Got dataframe column type and checked whether it is float and int.

**Task 3:** Get n-gram of categorical variable and try different models for improving accuracy (6)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Start Date:** 2nd November 2019
- **End Date:** 6th November 2019
- **Blockers:** None
- **Comment:** Used TfidfVectorizer to get ngrams and trained with different models.

#### Use Case 2: Performing Exploratory Data Analysis on user data set 

**Task 1:** Perform Exploratory data analysis for categorical columns and incorporate the results into the file and give it to the user for reference (7)
- **Assigned:** Nita Radhakrishnan (@nradhak2)
- **Status:** Completed
- **Blockers:** None
- **Comment:** 
    - Extended EDA to performed value counts on categorical columns in dataset before factorisation as part of the EDA
    - Factorised the categorical and performed correlation count, data set description using summary statistics, descriptive  analysis and normality tests
 
**Task 2:** Perform Unit Testing on Use case 2 (3)
- **Assigned:** Nita Radhakrishnan (@nradhak2)
- **Status:** Completed 	
- **Blockers:** None
- **Comment:** 
    - Performed unit testing using one sample numerical data set and one sample categorical data set for Happy Flow and for Alternate Flow 
    - Updated use case to write results into a file with constant name to ease integration rather have dynamic file generation 

#### Use Case 3: To provide user with description of user-requested Library/API and corresponding functions

**Task 1**: Improve the Usecase 3 retrieval of information about functions. (5)
- **Assigned:** Manikanta (@vnukala2)
- **Status**: Completed
- **Blockers**: None 
- **Comment**:

**Task 2:** Test all the integrated functionality works according to the Usecases and fix if any abnormalities (5)
- **Assigned:** Manikanta (@vnukala2)
- **Status**: Completed
- **Blockers**: None 
- **Comment**:

#### Integration 

**Task 1:** Proceed with the documentation of the Milestone 2 (3)
- **Assigned:** Rajshree (rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 


**Task 2:** Integrating the bot finally with all the backend use cases to respond without any error. (3)
- **Assigned:** Rajshree (rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 

**Task 3: Understand and working on the testing of the bot in Phase 2 (4)
- **Assigned:** Rajshree (rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 



