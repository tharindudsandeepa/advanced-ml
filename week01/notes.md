# Week 01 – Linear regression

## Key concepts

Machine Learning

    Traditional Programming: Write the Rules (Algorithm) manually and feed in Data (Inputs) along with those rules into the computer, and the computer computes the Outputs.
    
    Machine Learning: Feed both the Data and the known Outputs into the computer. The machine learning algorithm analyzes them to infer the underlying Function that maps inputs to outputs.

Machine Learning Pipeline:

    Data Collection -> Preprocessing -> EDA -> Feature Engineering -> Model Selection ->  Training -> Evaluation -> Deployment

ML Subdomains:

    Supervised Learning: Trains on labeled datasets to map inputs to target outputs.

    Unsupervised Learning: Discovers hidden structures or clusters in unlabeled data.

    Semi-Supervised Learning: Combines a small set of labeled data with larger amounts of unlabeled data.

    Reinforcement Learning: Uses an agent interacting with an environment to maximize cumulative feedback rewards.

Linear Regression:

    y = beta_1(x) + beta_0

    beta_0: The expected value of y when x = 0 (when input features have no effect).

    beta_1: The expected change in y for every 1 unit change in x.


Error vs Loss Function


    Error: The raw difference of predicted value and real value for a single data point.

        epsilon = y_i - y_hat

            y_i     = real value
            y_hat   = predicted value
            epsilon = error
    
    Loss: loss is a mathematical function that transforms that error into a single score used to train and optimize the model


Loss Metrics

    ** A simple sum or average of raw errors cancels positive and negative residuals out toward zero.**


    MAE (Mean Absolute Error): Measures average absolute magnitude of errors

        MAE = [SUM (y_i - y_hat) ]/total_number_of_data

    MSE (Mean Squared Error):Averages squared of errors

        MSE = SUM [(y_i - y_hat)^2]/total_number_of_data

    RMSE (Root Mean Squared Error): Squre Root of MSE.

        RMSE = SQRT (MSE)
    

## Insights

-Machine learning algorithms make assumptions about the underlying data distribution. If real world behavior violates these core assumptions (eg -  applying a linear model to non linear patterns), the model cannot automatically correct itself.

-Standard linear regression assumes linear relationships between independent features and target variables. non linear curves or binomial distributions require generalized models  rather than linear regression.

-Loss is calculated as a function of the model parameters. optimization algorithms navigate this loss surface to find the parameter weights that minimize global cost.

-Combining automated agent pre labeling with domain expert review creates an efficient hybrid pipeline that overcomes manual annotation bottlenecks.

