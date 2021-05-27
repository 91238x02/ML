# Index for Kaggle_Titanic
<br>

## Source
https://www.kaggle.com/c/titanic
<br><br>

## Results
- Kaggle Rank
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/kaggle_rank.png?raw=true" height="400px" width="650px">  
<br>

- Kaggle Score
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/Score.png?raw=true" width="650px">  
<br><br>

## Directory index
- Func_T1.py : Functions for pre-processing used 'Kaggle_Titanic.ipynb' script
- Kaggle_Titanic.ipynb : Main script contain Visualizations
- Titanic_Submission_res.txt : options for top7% submission csv file
- XGB_options.txt : about hyper parameters
- env.txt : python env setting (ML_1)
- top7%.csv : Submission csv file for kaggle
<br><br><br>


## Dataframe : Pre-processing
### [1]Raw dataframe : 891 rows x 12 columns
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/raw.PNG?raw=true" width="650px">
<br>     
     
### [2]Pre-processed dataframe : 891 rows x 12 columns
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/pre-processed.png?raw=true" width="650px"><br> 
- Create 4 columns : child_women, fare55, Title, Age_mean
- Drop 4 columns : PassengerId, Name, Ticket, Cabin
<br>


## Preview (Visualizations)
### [1]Boxplot : Survived
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/boxplot.png?raw=true" width="400px">  
<br>

### [2]Correlation : int type variables
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/cor.png?raw=true" width="400px">  
<br>

### [3]Feature importances : with XGBoost
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/importance.png?raw=true" width="800px">  
<br>

### [4]Pie Chart : Survived-Name(preprocessed)
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/pie_chart.png?raw=true" width="800px">  
<br>

### [5]Bar Chart
- Survived-Age(categorical)~Sex
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/bar_chart.png?raw=true" width="800px">  
<br>

- Survived-Pclass~Sex
<img src="https://github.com/LemonChocolate/ML/blob/main/Kaggle_Titanic/img/bar_chart_2.png?raw=true" width="400px">
<br>




