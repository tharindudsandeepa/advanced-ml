# Week 03 – Machine Learning Model export and Inference

## Overall ML Workflow

        Dataset
            |
            v
        Identify Variables
            |
            +-----------------------+
            |                       |
            v                       v
        Numerical Variables    Categorical Variables
            |                       |
            v                       v
        StandardScaler          OneHotEncoder
            |                       |
            +-----------+-----------+
                        |
                        v
                    Pipeline
                        |
                        v
                Machine Learning
                    Model
                        |
                        v
                Save using Joblib
                        |
                        v
                FastAPI API
                        |
                        v
                Pydantic
            Request Validation
                        |
                        v
                ML Prediction
                        |
                        v
                    Uvicorn
                        |
                        v
                    Client

## Key concepts

    Numerical Variables

        Numerical variables can have different scales.

        For example:
            - Weight can have values in thousands.
            - Acceleration can have values around 10–20.
            - Horsepower can have values in hundreds.

        If variables have very different scales, variables with larger numerical values can have a greater influence on the model during training.

        However, the actual importance of a feature does not necessarily depend on its numerical scale.

        To avoid this problem, we can use StandardScaler to transform numerical variables into a similar scale.

    StandardScaler

        StandardScaler standardizes numerical features so that they are centered around a mean of 0 with a standard deviation of 1.

        We use StandardScaler for numerical variables.


    Categorical Variables

        Categorical variables represent categories or groups rather than continuous numerical values.

        Examples:

            Country
            Car origin
            Gender
            Type

        Machine learning models generally work with numerical values, so categorical values need to be converted into numerical representations.

        For this, we can use OneHotEncoder.

    One-Hot Encoding

        One-hot encoding converts categorical values into multiple binary numerical features.

        For example:

            Origin
            USA
            Europe
            Japan


        Can become:

            USA    Europe    Japan
            1       0         0
            0       1         0
            0       0         1


        Each category gets its own column.

            A single row contains a value of 1 for the corresponding category and 0 for the other categories.

            This numerical representation is called a one-hot vector.

        Why One-Hot Encoding?

            Computers and machine learning models work with numerical values. One-hot encoding allows categorical information to be represented numerically without implying that one category is greater or smaller than another.

        We use OneHotEncoder for categorical variables.

    Preprocessing

        Before training a machine learning model, different types of variables may require different preprocessing techniques.

            Numerical Variables
                    |
                    v
            StandardScaler
                    |
                    v
            Scaled Numerical Features


            Categorical Variables
                    |
                    v
            OneHotEncoder
                    |
                    v
            Numerical Features

        Therefore, we can apply the appropriate preprocessing technique to each type of variable.

    Pipeline

        A Pipeline allows us to bundle multiple machine learning steps together into a single workflow.

            Input Data
                |
                v
            Preprocessing
                |
                +--> StandardScaler (Numerical Variables)
                |
                +--> OneHotEncoder (Categorical Variables)
                |
                v
            Machine Learning Model
                |
                v
            Prediction

        The pipeline ensures that the same preprocessing steps used during training are also applied when making predictions.

        This is especially useful when deploying a machine learning model because we can save the preprocessing and model together instead of managing them separately.

## What I learnt

    Joblib

        joblib can be used to save and load Python objects, including trained machine learning models.

    We can use it to export a trained model to a file.

        joblib.dump(model, "model.joblib")

    Later, we can load the model:

        model = joblib.load("model.joblib")

    This allows us to train the model once and then use the saved model for predictions without training it again.


    FastAPI

        FastAPI is a Python web framework used to build APIs.

    We can use FastAPI to expose our machine learning model through an API.


            Client
            |
            | HTTP Request
            v
            FastAPI
            |
            v
            ML Model
            |
            v
            Prediction
            |
            v
            HTTP Response


    This allows other applications to send input data to our API and receive predictions from the machine learning model.


    Pydantic

        Pydantic is used by FastAPI for data validation and data parsing.

    We can define the expected request structure using a Pydantic model.

            class PredictionRequest(BaseModel):
                weight: float
                horsepower: float
                model_year: int


    If the client sends invalid or missing data, FastAPI/Pydantic can validate the request and return an appropriate error.

                Request
                |
                v
                Pydantic Validation
                |
                v
                Valid Data
                |
                v
                ML Model


    Uvicorn

        Uvicorn is an ASGI server used to run FastAPI applications.

        FastAPI defines the API application, while Uvicorn runs the application and handles incoming HTTP requests.

## Practical / code

    poetry run python -m uvicorn server:app --host 127.0.0.1 --port 8000

        Meaning:

        poetry run
            -> Run the command using the Poetry environment

        python -m uvicorn
            -> Run Uvicorn as a Python module

        server:app
            -> Use the "app" FastAPI object from server.py

        --host 127.0.0.1
            -> Run the server on the local machine

        --port 8000
            -> Run the API on port 8000

        The API can then be accessed locally through: http://127.0.0.1:8000

## Questions / things to revisit

## Overall Machine Learning Deployment Flow
