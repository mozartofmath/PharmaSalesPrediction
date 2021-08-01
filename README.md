# Sales Data Analysis
## Introduction
Rossmann Pharmaceuticals is a pharmaceutical chain that has 1115 stores.
Rossmann Pharmaceuticals’ finance team wants to forecast sales in all their 1115 stores across several cities six weeks ahead of time.
The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.
In this project, we are building an end-to-end product that delivers this prediction to analysts in the finance team.

# Models
We trained three types of models for this project
<ol>
<li>Linear Regression</li>
<li>Random Forest Regression</li>
<li>LSTM Regression</li>
</ol>

## Linear Regression
<p>In linear regression is a linear approach to modeling the relationship between a scalar response and one or more explanatory variables (also known as dependent and independent variables). The case of one independent variable is called simple linear regression; for more than one, the process is called multiple linear regression. In this project, we built multiple linear regression model. We had 18 independent variables and 1 dependent variable, which was the amount of money a store earned during the given day (sales).</p>

## Random Forest Regression
<p>Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. Random decision forests correct for decision trees' habit of overfitting to their training set. Since the problem we wanted to solve in this project is a decision problem, we used the random forest regression model.</p>

## LSTM Regression
<p>Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can process not only single data points (such as images), but also entire sequences of data (such as speech or video). In our project, since we are interested in predicting the daily sales of pharmaceutical stores, we can consider the daily earnings of the stores as a time series or a sequence. It is for this reason that we decided to use LSTMs in our regression model. When training this model, we decided to use the data for only one store because different stores have different customer behaviors and since the order of the data matters, a sequence that has data from different stores will skew our result. That’s why we decided to train a separate LSTM model for each store.</p>

## Code
The code of our analysis can be found in the **notebooks** folder. The data preprocessing and visualization parts can be found in the **Task1.ipynb** jupyter notebook. The code for training the Linear Regression and the Random Forest Regression models can be found in the **Task2.ipynb** jupyter notebook. The code for training the LSTM Regression model can be found in the **DeepLearning.ipynb** jupyter notebook. The data is stored in the **data** folder. The trained models are stored in the **models** folder.

## Dependencies
To install the necessary dependencies, execute the command 
```$ pip install -r requirements.txt"```
