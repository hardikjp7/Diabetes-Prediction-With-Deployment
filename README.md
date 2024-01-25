# Diabetes-Prediction-With-Deployment

# Diabetes Prediction Project

This project focuses on predicting diabetes using machine learning techniques. The model predicts whether a person is diabetic or non-diabetic based on various input features. The project includes both Flask and Streamlit implementations for different deployment options.

## Clone and Run the Project

Follow these steps to clone and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/hardikjp7/Diabetes-Prediction-With-Deployment.git
cd diabetes-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Flask App (app.py)
```bash
python app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your web browser.

### OR

### 4. Run Streamlit App (app1.py)
```bash
streamlit run app1.py
```
Visit the provided local URL in your web browser.

## Project Details

- **dataset:** Folder containing the dataset used for training the model.
  
- **Model:**
  - **standardScalar.pkl:** Pickle file containing the StandardScaler object used to scale input features.
  - **modelForPrediction.pkl:** Pickle file containing the trained machine learning model for diabetes prediction.

- **notebook:**
  - **Logistic_Regression.ipynb:** Jupyter notebook file containing the development and training of the diabetes prediction model using Logistic Regression.

- **templates:**
  - **home.html:** HTML template for the home page.
  - **index.html:** HTML template for the index page (used by Flask app).
  - **single_prediction.html:** HTML template for displaying the prediction result (used by Flask app).

## Usage

- For the Flask app, enter the required details on the web form and click the "Predict" button to see the result.

- For the Streamlit app, use the number input fields to enter the required details and click the "Predict" button to see the result.

Feel free to explore, modify, and enhance the project according to your needs!

## Deployment

This project can be deployed via Flask or Streamlit. Choose the deployment option that best fits your requirements:

- **Flask Deployment:** The Flask app can be deployed using any suitable web server, such as Gunicorn or uWSGI. Configure the server to run the Flask app.

- **Streamlit Deployment:** Use Streamlit to deploy the Streamlit app. You can deploy it to Streamlit Sharing, Heroku, or other platforms that support Streamlit apps.

Make sure to update the deployment settings and configurations based on your hosting environment.

**Note:** Ensure that the necessary dependencies are installed, and the correct Python version is used for deployment.
