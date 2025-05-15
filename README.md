ML Package with Flask API

A Python package and Flask-based REST API for building and serving machine learning models for classification and regression tasks. Includes support for Docker deployment.

------------------------------------------------------------
FEATURES
------------------------------------------------------------
- Generates synthetic datasets (via scikit-learn)
- Supports both regression and classification problems
- Trains models (Linear Regression or LDA)
- Computes statistics (mean, std, correlations)
- Returns predictions and error metrics as JSON
- Dockerized for easy deployment
- Flask-based REST API

------------------------------------------------------------
INSTALLATION (Python Package Only)
------------------------------------------------------------
Install via pip:

    pip install ml_package-0.1.0.tar.gz

------------------------------------------------------------
PACKAGE USAGE
------------------------------------------------------------
    from ml_package import question2

    # Generate a dataset
    X, y = question2.generate("classification", n_samples=100, n_features=5)

    # Compute statistics
    stats = question2.statistics(X, y)

    # Train a model
    model, error = question2.learn("classification", X, y)

    # Make predictions
    predictions = question2.predict(model, "classification")

------------------------------------------------------------
API USAGE
------------------------------------------------------------
Endpoint:
    GET /process

Query Parameters:
    n_samples: number of data points (default: 100)
    n_features: number of features (default: 5)
    problem: "classification" or "regression"

Example:
    curl "http://127.0.0.1:5000/process?n_samples=100&n_features=5&problem=classification"

Response:
    - Model predictions
    - Error rate
    - Dataset statistics (means, stds, correlations)

------------------------------------------------------------
RUNNING WITH DOCKER
------------------------------------------------------------
Requirements:
    - Python 3.10+
    - Docker
    - Git

Steps:
1. Clone the repo:

    git clone https://github.com/KeneAli/ml-api-docker.git
    cd ml-api-docker

2. Build the Docker image:

    docker build -t ml-api .

3. Run the container:

    docker run -p 5000:5000 ml-api

The API will be available at:

    http://127.0.0.1:5000/process

------------------------------------------------------------
DEPENDENCIES
------------------------------------------------------------
- numpy
- scikit-learn
- matplotlib
- plotly
- flask
