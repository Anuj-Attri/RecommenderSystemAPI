# RecommenderSystemAPI
A Flask-based API for a recommendation system that predicts results based on user input features. The API uses a pre-trained recommendation model (Recommender.pkl) and is designed for ease of use and deployment.

## Project Structure
```
RecommenderSystemAPI/
├── data/
│   ├── Data.xlsx        # Input dataset 
│   ├── Data.csv             
│
├── model/
│   ├── Recommender.pkl      # Pre-trained recommendation model
│
├── app.py                   
├── recommender_security.ipynb 
├── LICENSE                  
├── README.md                
```
              
## Features

- **Prediction API**: Accepts POST requests with JSON input and returns model predictions.
- **Simple Setup**: Flask-based API that can be run locally or deployed.
- **Real-World Data**: Includes example datasets for testing (`Data.csv`, `Data.xlsx`).
- **Notebook Support**: A Jupyter Notebook (`recommender_security.ipynb`) for analyzing and refining the model.

---

## Requirements

- Python 3.8+
- Flask
- joblib
- pandas
- numpy

## Installation
1. Clone the repository
```
git clone https://github.com/Anuj-Attri/RecommenderSystemAPI.git
cd RecommenderSystemAPI
```

2. Create a virtual environment (optional):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```