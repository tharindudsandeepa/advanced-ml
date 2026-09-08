# Week 02 – Exploratory Data Analysis 

## Key concepts

Variable Types
    Quantitative: Data that is numeric and represents a measurable amount.

        Discrete: countable values, usually whole numbers
            Example: number of students in a class.

        Continuous: can take any value within a range, including decimals. 
            Example: height, temperature, weight.

    Qualitative: data that describes categories or labels, not amounts.

        Ordinal: Categories that have a meaningful order/ranking. 
            Example: education level (high school < bachelor's < master's).

        Nominal: Categories with no inherent order, just labels. 
            Example: eye color, gender, city name.

EDA

	Univariate analysis
        histogram - we can identify wheather values are normal distribution or not.

    skewness -  if normal distribution skewness should be less
		        if skew to right then value should be positive
                simple linear regression  should follow normal distribution

    box plot -  can identify wheather values are same scale or not.distributions
                we can identify outliers. values that violates common pattern
                we need to decide wheather we get the outlier data to train or not.

	Bi-variate analysis

            Analysis of the connection between two variables.

	Correlation analysis    
        heatmap of pearson correlation

            -1<= corr(x,y) <=1

                if corr(x,y) =1 OR corr(x,y) = -1 >>>> Strong relationship
                if corr(x,y) more likely equal to zero then no relationship

            |corr(x,y)|>=0.7 consider as good correlation between two variables.


        Multicollinearity: 
            When two or more predictor (X) variables are strongly correlated with each other, rather than being independent. This is a problem for linear regression because it makes it hard for the model to isolate each variable's individual effect on the target.


## What I learnt

Train/Test split ratio depends on dataset size.

Smaller datasets use a larger test share, around 70:30, to ensure the test set has enough data to reliably evaluate the model.

Very large datasets (millions of rows) use a much smaller test share, around 99:1, since even 1% of millions of rows is still plenty of data to get a stable, trustworthy evaluation while maximizing data available for training.


## Practical / code



## Assignment / homework

### Task 3 — EDA Findings

Relationships between predictors and Target variable (Y1)

    X5 (Overall Height) has the strongest relationship (correlation) of 0.89 with Y1. Taller buildings has higher heating load.

    X4 (Roof Area) is nearly as strong but negative correlation of -0.86.Larger roof area has lower heating load.


Skewness and Outliers

    No boxplot  shows any points beyond the whiskers.No outliers in any of the six quantitative predictors.

    X1,X2 and X3 are unimodal distribution with right skewed. (Slight positive skew)

    X4,X5 and X6 are multi modal distribution.


Multicollinearity

    X1 and X2: -0.992 — extremely strong negative correlation
    X4 and X5: -0.973 — extremely strong negative correlation
    X2 and X4: 0.881 — strong positive correlation
    X2 and X5: -0.858 — strong negative correlation
    X1 and X5: 0.828 — strong positive correlation


    As a result, multicollinearity may affect the stability and interpretation of the regression coefficients, making it difficult to determine the individual contribution of each predictor to Heating Load.

### Task 4 — Model Performance

    
    Test-set metrics:
    R2 = 0.915
        Model captures 91.5% of the pattern in why Heating Load differs from building to building. The remaining 8.5% is unexplained.

    RMSE = 2.99
        2.99 means on average, across all your test predictions, the model's prediction is off from the true Heating Load by about 2.99 units.
    MAE = 2.15
        On average, the model's predicted Heating Load is off from the actual value by about 2.15 units.

    
Train vs Test Comparison

    Train R2:   0.9150
    Train RMSE: 2.9202
    Train MAE:  2.0236

    Test R2:    0.9150
    Test RMSE:  2.9894
    Test MAE:   2.1471

    R2 gap (train - test):   0.0001
    RMSE gap (test - train): 0.0692

### Task 5 — Parameter Interpretation

X1 (Relative Compactness):  -64.91	
    Holding everything else fixed, a 1 unit increase in compactness is associated with a 64.91 drop in Heating Load.
X2 (Surface Area):	-0.06	
    1 square meter increase in surface area is associated with a 0.06 drop in Heating Load, holding others fixed.
X3 (Wall Area):	0.04	
    1 square meter increase in wall area is associated with a 0.04 rise in Heating Load.
X4 (Roof Area):	-0.05	
    1 square meter increase in roof area is associated with a 0.05 drop in Heating Load.
X5 (Overall Height):	4.01	
    1 unit increase in building height is associated with a 4.01 rise in Heating Load.
X7 (Glazing Area):	20.21	
    1 unit increase in glazing area  is associated with a 20.21 rise in Heating Load.
Intercept:	86.25	
    The predicted Heating Load when all predictors has zero effect.

## Questions / things to revisit


