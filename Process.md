# PROCESS 

## Iteration 1 (Wed Oct 23-- Fri Nov 1):

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

  
### Meeting Notes (Mon Oct 28th 2019)
**Key Decisions:**
  - Had a discussion about the progress of tasks/stories.
  - Discussed about the difficulties in developing the tasks and helped each other in resolving the issues.

**Attendees:**
- Sandeep Kundala 
- Nita Radhakrishnan 
- Rajshree Jain 
- Manikanta NVSR 

### Story Creation and Assignment 

#### Use Case 1: Selecting best model for the dataset
**Task 1:** Program to accept the csv file and check whether target column is present (2)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Blockers:** None
- **Comment**:
    * Used Python Pandas module to read the CSV file and check the columns.

**Task 2:** Train the dataset using different ML Algorithms and choose the best model (8)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
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
- **Blockers**: Descriptive plots which are a part of EDA cannot be written into the text file 
- **Comment**:
    - Performed non-graphical exploratory data analysis
    - Described the data set on basis of target variable and provided summary statistics
    - Calculated descriptive statistics for data set 
    - Calculated correlation values between variables in dataset using 3 different methods
    - Tested Normality of data using 3 different tests  

#### Use Case 3: To provide user with description of user-requested Library/API and corresponding functions 
**Task 1:** Develop the database CSV File which includes ML Libraries and Functions in Python. (5)
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
- **Assigned:** Rajshree (@rjain27)
- **Status:** Completed
- **Blockers:** None 
- **Comments:** 
   - Implement the working of bot in such a way that it intelligently selects the use cases to be selected for all types of inputs by the user. 

**Task 2:** Determine all the use cases and check how the bot should handle the requests and responses in all the cases.(6)
- **Assigned:** Rajshree (@rjain27)
- **Status:** Completed
- **Blockers:** None 
- **Comments:** 
   - Analyze all the use cases and work with other team members so as to understand what type of functionality will the bot actually require.

### Practices  
  - We followed pair programming while developing the tasks. For example, Task 2 in Usecase 3 is implemented by @vnukala2 while @nradhak2 guides the steps.
  - We followed Agile practices while developing the tasks. For example, Everytime a task is completed we did an end to end testing for that task and resolved any integration issues occurred.
  
### Process Reflection 
Overall, the sprint was carried out smoothly with great co-operation from all team-members. However, coming to a common sensus regarding the availabilty of each of the team members was a challenge since each team-member was invloved in other tasks that occupied their time.  Nevertheless, the team managed to fit regular scrum meetings in their schedule and stay updated with the activities of the team-members, for this sprint  

## Iteration 2 (Sat Nov 2--Fri Nov 8th):

**Division of Tasks using kanban board:**
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/kanban2.jpg)

### Meeting Notes (Sat Nov 2nd 2019)

**Key Decisions:**
  - Discussed development of use cases in second iteration and decided to perform coverage testing on completion of use cases development
  - Divided development of use cases in second sprint into stories
  - Assigned stories to each of the teammates and discussed deadlines for completion
  
**Attendees:**
- Sandeep Kundala 
- Nita Radhakrishnan 
- Rajshree Jain 
- Manikanta NVSR 

### Meeting Notes (Wed Nov 6th 2019)
**Key Decisions:**
  - Had a discussion about the progress of tasks/stories and if there is anything left from the iteration 1, that should be completed.
  - Discussed how to proceed with coverage testing and if there is any issue in running the use cases or, if there is any blocker that is obstructed from further testing.

**Attendees:**
- Sandeep Kundala 
- Nita Radhakrishnan 
- Rajshree Jain 
- Manikanta NVSR 

### Story Creation and Assignment 

#### Use Case 1: Selecting best model for the dataset

**Task 1:** Log the tasks performed by the bot in the backend and give it to the user for reference (1)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Blockers:** None
- **Comment:** File handling operation - all the logs are saved in file *modelSelectionProcess.txt*

**Task 2:** Factorize and update the dataset if Categorical column is present (3)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Blockers:** None
- **Comment:** Got dataframe column type and checked whether it is float and int.

**Task 3:** Get n-gram of categorical variable and try different models for improving accuracy (6)
- **Assigned:** Sandeep Kundala (@skundal)
- **Status:** Completed
- **Blockers:** None
- **Comment:** Used TfidfVectorizer to get ngrams and trained with different models.

#### Use Case 2: Performing Exploratory Data Analysis on user data set 

**Task 1:** Perform Exploratory data analysis for categorical columns and incorporate the results into the file and give it to the user for reference (7)
- **Assigned:** Nita Radhakrishnan (@nradhak2)
- **Status:** Completed
- **Blockers:** Descriptive plots which are a part of EDA cannot be written into the text file 
- **Comment:** 
    - Performed non-graphical exploratory data analysis on categorical data as well 
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

**Task 1**: Improve the Usecase 3 retrieval of information about functions. (4)
- **Assigned:** Manikanta (@vnukala2)
- **Status**: Completed
- **Blockers**: None 
- **Comment**:
    - Added functionality of the retrieval of information about functions and integrated bot interaction.

**Task 2:** Test all the integrated functionality works according to the Usecases and fix if any abnormalities (6)
- **Assigned:** Manikanta (@vnukala2)
- **Status**: Completed
- **Blockers**: None 
- **Comment**:
    - Tested all the functionalities and fixed all the abnormalities occurred.

#### Integration 

**Task 1:** Proceed with the documentation of the Milestone 2 (3)
- **Assigned:** Rajshree (@rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 
  - Understand the deliverables of Phase 2 and work on the documentation simultaneously.

**Task 2:** Integrating the bot finally with all the backend use cases to respond without any error. (3)
- **Assigned:** Rajshree (@rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 
  - Handled the bot integration with the final working of use case 1, use case 2, and use case 3.
  - Looked into how the bot should handle the requests and responses in case of both the actual flows and the alternate flows
  
**Task 3:** Understand and working on the testing of the bot in Phase 2 (4)
- **Assigned:** Rajshree (rjain27)
- **Status**: Completed
- **Blockers**: None 
- **Comments**: 
  - Understand the full working of bot with use case 1, use case 2, and use case 3 to start building the coverage testing and unit tests.
  
 **Practices**:  
  - We followed pair programming while working on usecases. For example, Task 1 in Usecase 3 is implemented by @vnukala2 while @rjain27 discussed all the steps for implementation of the use case.
  - Following the scrum methodology we could develop the project with iterative devdelopment, where short meetings ensured that important tasks are prioritized based on feedback in the scrum meetings.
  
### Testing

**Coverage Test:**

![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/Coverage_test_report.jpeg)


