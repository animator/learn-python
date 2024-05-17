# Movie Recommended System Using ML in Python

To provide a structured breakdown of the concepts used in writing a movie recommendation system, we'll assume a typical example where the system involves data processing, model training, and prediction steps. Here is a comprehensive division of the concepts, assuming a basic content outline for a movie recommendation system:

## 1. Data Collection and Preprocessing
### Importing Libraries
- **Purpose:** Use libraries to handle data manipulation, model building, and evaluation.
- **Example:**
  ```python
  import pandas as pd
  import numpy as np
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import mean_squared_error
  ```

### Loading Data
- **Purpose:** Load datasets containing movie ratings, movie details, and user information.
- **Example:**
  ```python
  ratings = pd.read_csv('ratings.csv')
  movies = pd.read_csv('movies.csv')
  ```

### Data Cleaning
- **Purpose:** Handle missing values, duplicates, and inconsistent data.
- **Example:**
  ```python
  ratings.dropna(inplace=True)
  ```

### Data Merging
- **Purpose:** Combine multiple datasets for comprehensive analysis.
- **Example:**
  ```python
  data = pd.merge(ratings, movies, on='movieId')
  ```

### Exploratory Data Analysis (EDA)
- **Purpose:** Gain insights into data through visualizations and statistical analysis.
- **Example:**
  ```python
  import matplotlib.pyplot as plt
  data['rating'].hist()
  ```

## 2. Feature Engineering
### Encoding Categorical Variables
- **Purpose:** Convert non-numeric data into a numeric format suitable for model input.
- **Example:**
  ```python
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  data['movieId'] = le.fit_transform(data['movieId'])
  data['userId'] = le.fit_transform(data['userId'])
  ```

### Creating User-Item Matrix
- **Purpose:** Create a matrix where rows represent users and columns represent movies, with ratings as values.
- **Example:**
  ```python
  user_item_matrix = data.pivot(index='userId', columns='movieId', values='rating')
  ```

## 3. Model Building
### Choosing a Model
- **Common Models:** Collaborative Filtering (User-Based, Item-Based), Matrix Factorization (SVD).
- **Example:**
  ```python
  from sklearn.decomposition import TruncatedSVD
  ```

### Model Training
- **Purpose:** Train the chosen model on the dataset.
- **Example:**
  ```python
  svd = TruncatedSVD(n_components=50)
  matrix = user_item_matrix.fillna(0)
  svd.fit(matrix)
  ```

## 4. Making Predictions
### Generating Recommendations
- **Purpose:** Use the trained model to predict ratings and recommend movies.
- **Example:**
  ```python
  user_ratings = svd.transform(matrix)
  predicted_ratings = svd.inverse_transform(user_ratings)
  ```

### Selecting Top Recommendations
- **Purpose:** Identify and rank the top movies for each user.
- **Example:**
  ```python
  def recommend_movies(user_id, num_recommendations):
      user_index = user_id - 1  # assuming user_id starts from 1
      sorted_indices = np.argsort(predicted_ratings[user_index])[::-1]
      top_movies = sorted_indices[:num_recommendations]
      return top_movies
  ```

## 5. Model Evaluation
### Splitting Data
- **Purpose:** Split the data into training and testing sets to evaluate model performance.
- **Example:**
  ```python
  train_data, test_data = train_test_split(data, test_size=0.2)
  ```

### Evaluation Metrics
- **Common Metrics:** RMSE (Root Mean Squared Error), MAE (Mean Absolute Error).
- **Example:**
  ```python
  def calculate_rmse(true_ratings, predicted_ratings):
      return np.sqrt(mean_squared_error(true_ratings, predicted_ratings))
  ```

## 6. Deployment
### Saving the Model
- **Purpose:** Save the trained model for future use.
- **Example:**
  ```python
  import joblib
  joblib.dump(svd, 'movie_recommendation_model.pkl')
  ```

### Loading the Model
- **Purpose:** Load the saved model to make predictions.
- **Example:**
  ```python
  model = joblib.load('movie_recommendation_model.pkl')
  ```

### Creating an Interface
- **Purpose:** Build a user interface to interact with the recommendation system (e.g., web app).
- **Example:** Using Flask for a web application.
  ```python
  from flask import Flask, request, render_template
  app = Flask(__name__)

  @app.route('/recommend', methods=['POST'])
  def recommend():
      user_id = request.form['user_id']
      recommendations = recommend_movies(user_id, 10)
      return render_template('recommendations.html', movies=recommendations)
  ```

This breakdown provides a comprehensive guide to the various concepts and steps involved in building a movie recommendation system, from data preprocessing to deployment.
