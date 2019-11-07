# PROCESS 

### Iteration 1:
**Use Case 1: Selecting best model for the dataset**
**Task 1:** Program to accept the csv file and check whether target column is present (2)
- **Assigned:** @skundal
- **Status:** Completed
- **Blockers:** None
- **Comment:** Used Python Pandas module to read the CSV file and check the columns.

**Task 2:** Train the dataset using different ML Algorithms and choose the best model (8)
- **Assigned:** @skundal
- **Status:** Completed
- **Blockers:** XGBoost Classifier Installation - Incompatible with PyCharm
- **Comment:**
 	- Preprocess the dataset and split the dataset into training and testing dataset.
     - Used SciKit library to train the models.
     - XGBoost Classifier - The support to XGBoost Classifier is not present in PyCharm. Tested the code using terminal window (command prompt)



### Iteration 2:
**Use Case 1: Selecting best model for the dataset**

**Task 1:** Log the tasks performed by the bot in the backend and give it to the user for reference (1)
- **Assigned:** @skundal
- **Status:** Completed
- **Blockers:** None
- **Comment:** File handling operation - all the logs are saved in file *modelSelectionProcess.txt*

**Task 2:** Factorize and update the dataset if Categorical column is present (3)
- **Assigned:** @skundal
- **Status:** Completed
- **Blockers:** None
- **Comment:** Got dataframe column type and checked whether it is float and int.

**Task 3:** Get n-gram of categorical variable and try different models for improving accuracy (6)
- **Assigned:** @skundal
- **Status:** Completed
- **Blockers:** None
- **Comment:** Used TfidfVectorizer to get ngrams and trained with different models.



