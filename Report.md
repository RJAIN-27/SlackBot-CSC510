# Report 

## State of affairs addressed by our bot:
With the explosion of Machine Learning applications in every field, it has become important for every organization to use and understand these applications and APIs, effectively.

There are many such APIs and the popular ones are those offered by Python. But understanding the usage of these APIs, and in general the process of Machine Learning is still unclear to many which makes it complex for users who are not experts. 

The information available online regarding the usage of such APIs and libraries is vast and diverse. It is tedious to scout around a multitude of these sources and nail down on a satisfying answer and proceed with the implementation. Therefore, having a solution that answers questions regarding these libraries and the implementation on datasets, posed by users of these APIs, in a concise and satisfying manner, all under the same roof, especially when the users are unclear about what has to be done with a dataset, is certainly beneficial. This is what our bot aims at achieving. 

Our bot, L.I.B.R.A. (Library-Intensive Bot for Recommendation Assistance) helps the users in understanding the ML APIs of Python in a concise and systematic manner, by responding to the user’s requests. The bot is also primarily developed to aid the users in understanding the dataset, as well as what model has to be applied on the users' dataset, by applying a series of elegant machine learning techniques internally on the dataset. This way the users get the solution to their questions all under one roof.

## Primary Features of the bot
Our bot hosts three primary features. They are as given below. 

1. It helps the users understand what model fits best for the users’ dataset, by applying model selection techniques in machine learning. 
2. It helps the users understand the details of their dataset by performing exploratory data analysis.
3. It also helps the users understand the libraries and functions in machine learning offered by Python, by providing a description of these libraries/functions as requested by the user. 

The description of these features in action is as given below. 

### Feature 1: Model suggestion 
The user requests the bot to suggest a good model for the data set and then provides the bot with the dataset as well as the target column of the dataset. 
The bot then performs preprocessing and model selection by applying models like Linear Support Vector Classifier, K-Nearest Neighbour Classifier, Decision Tree Classifier, Naive Bayes Classifier, Adaboost Classifier, and Random Forest Classifier, on the dataset. 
Depending on the accuracy metrics of the model on the dataset, the bot returns the result of the model selection in a text file back to the user. 

****Screenshots**** 

### Feature 2: Analysis of the data set
The user requests the bot to analyse the user’s dataset and provides the bot with the dataset as well as the target column. 
The bot then performs descriptive analytics on the dataset and provides the result of this analysis, namely, summary statistics, correlation results, hypothesis testing for normality of the dataset and value counts, in a text file back to the user. 

****Screenshots****

### Feature 3: Knowing the libraries/functions in machine learning offered by Python
The user requests the bot for information about a particular library in machine learning and the bot fetches this information from a database and returns it to the user. 
If the user wants to know about a specific function in the library, then the user can provide the name of the function in the library. The bot then fetches this information as well and returns it to the user if this exists

****Screenshots****
## Process Reflection 
For the development of the project we followed the Agile Methodology. We began with the design phase and proceeded with the bot development and the final deployment, with continuous integration using Jenkins. 
### Design Phase
In this phase, we abstracted the concept of our project and designed the architecture and the use cases of the project. The storyboard and the wireframes we designed in this phase helped us understand the flow of the system that we were about to develop. This phase helped create a systematic starting point for the rest of the phases in our project development. 
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/design.png)
#### How this phase was helpful
This phase helped us in understanding the constraints and requirements of the project. Coming to a common consensus regarding the requirements at the initial stage helped us in the later stages since it we did not have to make major changes to our architecture during the development. 
#### Challenges in this phase and how we overcame it
Understanding the requirements was initially challenging since each of the team members had different interpretations. But over a few meetings of brainstorming we finally came to a common understanding and documented it and proceeded with the development. 
### Bot phase
In this phase we began developing our bot. We integrated the bot platform of the bot and developed the interaction component of our bot. During this phase, we tested the integration of the components in our project with each other and with the slack environment. We developed the mocking infrastructure and tested the interaction with the bot platform and the working of our use cases using integration testing performed through Selenium in Java. 
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/bot.png)
#### How this phase was helpful
Implementing integration testing was useful because we were able to test different modules at the same time and understand how they behaved when connected in a group. By mocking these services, we were able to test expectations about code behavior for different variants of service implementation without actually using all of them, thereby also reducing the time taken for unit tests to run. 
#### Challenges in this phase and how we overcame it
The challenge we faced here was in automating testing using selenium as there were cases when the login ID and passwords were incorrectly populated and IDs of few elements in the web page weren't present. So we initially tried different frameworks but we eventually cracked the logic of accessing elements in webpage by digging further into inspecting the elements, and thereby able to use Selenium in Java to complete the automation in integration testing.

### Process phase 
In this phase, we implemented our use cases in two sprints by following the SCRUM-BAN process.
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/process.png)
#### How this phase was helpful
Following the SCRUM-BAN methodology for this milestone was very helpful since it gave us a systematic approach to implementing our use cases. The graphical interface in the form of the project boards helped us coordinate the tasks among the team members and follow up regularly. It made the process of tracking progress, hassle-free. It helped us raise red-flags whenever a certain task was not in the desired bucket/column which would have led to delay in providing necessary deliverables.
#### Challenges in this phase and how we overcame it
We faced challenges in identifying the common functions and modularizing the code for reusability. We later listed down the functions in each use case in order to organize the modularity of our codes clearly. In the future, we would list down the functions systematically in the initial stages of implementation in order to avoid confusion in the later stages.

### Deployment phase 
This being the final stage of development of our project, we deployed the fully developed version of our project. In this phase we handled the edge cases in our use cases and refactored our code for better readability and we deployed this final version of our project on the AWS environment using Ansible. In this phase we also implemented continuous integration by using Jenkins.
![](https://github.ncsu.edu/csc510-fall2019/CSC510-23/blob/master/resources/images/deployment.png)
#### How this phase was helpful
The continuous integration service in this phase that we implemented using Jenkins helped us regularly test and review the quality of our code. With the failure and success reports, we were able to enhance the quality of our code. 
With deploying our project on time, in real time, we essentially deliver the software on time to the market.
#### Challenges in this phase and how we overcame it
Our initial challenge with deploying our software was the absence of webhooks. Since we did not have complete user privileges to our repository, we did not have webhooks for deployment. After experimenting with deployment options, we decided to use Poll SCM instead, to continuously poll the repository for new commits, every 15 minutes. 

### Limitations
1.	Our bot currently performs model suggests and exploratory data analysis for numerical and nominal data only. 
2.	It also focuses only on machine learning libraries and functions available in Python. 
3.	The bot cannot follow up on operations previously performed. 

### Future Work
1.	The implementation of model suggestion and exploratory data analysis can be extended to apply to other types of datasets such as image content, time-stamped data, spatio-temporal data and so on.
2.	With the bot currently fetching information for libraries and functions from an existing database, this use case can be extended to directly pulling this information from the web, to make the information-retrieval more robust. 
3.	The interaction between the user and the bot can also be refined to enable smoother transfer of request and response, to avoid clunky transactions. 


## Presentation

Presentation video link: https://drive.google.com/open?id=1qmbrSdw1ZadvyhRsn_rWp_1haYhYcipq
