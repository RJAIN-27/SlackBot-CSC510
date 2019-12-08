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


## Presentation

Presentation video link: https://drive.google.com/open?id=1qmbrSdw1ZadvyhRsn_rWp_1haYhYcipq
