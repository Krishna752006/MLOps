# MLOps

Just Building Model = Not enough --> just 20% of whole business problem
MLE -> 10% ML and 90% Engineering (by **Elon Musk**)

## ML Teams

1. Discover Data - Develop Features - Train Models --> **Data Scientist**
2. Productionize Data Pipeline --> **Data Engineer**
3. Deploy Model --> **ML Engineer**
4. Integrate Servise --> **Product Engineer**
5. Set up Monitoring --> **Site Reliability Engineer**

This will be in a never ending loop in production environment or else model will start to decay, for example the Spammers change the stratergy of spam mails, reformulation od problem statement, business objective changes...

## ML in Real Life
![alt text](image.png)

## Why MLOps?
It is a set of practices that aims to deploy and maintain ML Models in production reliably and efficient.
MLOps -> Extension of DevOps to include ML and Data Science assets.

Simple ML -> Buildings
MLOps -> City made with Buildings

## Deployment Problems

Main Problem Starts after Deloyment... and not deployment itself.
53% of the sites are abandonded if they take more than 3 seconds to load(Think with Google Customer Insights) and do you really think the results will be delivered within 3 seconds....

Need to maintain Fairness -> Microsoft train a model on twitter data, became a racist and was taken down quickly.
Lack of Explainability and Audiability -> Lot of newer Ai rules are comming and need to make it to aloow all of them.
It is very slow -> Most of Data Scientist told that the minimum time would be a quarter of their whole time.

It can take like 2 days for model building and 1 week for deployment also.

## Model Centric vs Data Centric

Data Centric --> Holds the Model Fixed and iteratively improve the Data
Model Centric --> Hold the Data Fixed and iteratively improves the model

## Main MLops

What is the business problem we are trying to solve?
What is the cost of wrong prediction? eg: Overstock, leads to wastage of resources and Understock, leads to missed sales and unsatisfied customers.

We will here decompose the ales Forcasting problem as data gathering, historical sales analysis, market trend analysis and actual forccasting. AI/ML here would be used in actual forcasting task.

Here ROI (Return on Investment) can be estimated by comparing the potential increase in sales and decrease in wasted resources due to improved forcasts against the cost of developming and maintaining the AI/ML Solution.

## ML Canvas

A tool with 10 blocks that helps us structure and plan our ML Application Development.

1. **Value Proposition** -> Defining the problem, its importance and our end user persona. Eg: For (target customer) who (need), our (product/service) is (product category) that (benefit).
2. **Data Sources** -> Identifying Data Sources and also considering the hidden costs like data storage and purchasing external data.
3. **Prediction Task** -> Deciding ML Task like Unsupervised, Supervised, Anomaly Detection, Classification, Regression,... and also about the i/p, o/p and degree of model complexity.
4. **Feature Engineering** -> Working with domain experts to extract feature from raw data like MBBS for medical data, Mathematicians for math related data and so on... also has steps of Selecting the right data, Transforming them (Normalizaion), Crearting of newer data and Encoding.
5. **Offline Evaluation** -> Setting up metrics to evaluate the system pre-deployment. Understanding the model prediction errors and their impacts.
6. **Decisions** -> How end user interact with our predictions? Possible hidden costs, includeing human interventions
7. **Making Predictions**
8. **Collecting Data** -> Colecting newer data for re training and to avoid model decay. Cost of Collection and human intervation in labelling.
9. **Building Models** -> Deciding the frequency of model retraining. Planning for changes in tech stack and services.
10. **Live Evaluation and Monitoring** -> Setting Metrics to track system performance post deployment. Understanding corellation between model metrics and business metrics.
