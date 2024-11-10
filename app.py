import pandas as pd
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('home_team_encoder.pkl', 'rb') as file:
    home_encoder = pickle.load(file)
with open('away_team_encoder.pkl', 'rb') as file:
    away_encoder = pickle.load(file)

# Define available teams from encoder classes
teams = list(home_encoder.classes_)

# A mock function to get the recent performance data of a team
def get_team_form_stats(team, is_home, csv_file_path):
    df = pd.read_csv(csv_file_path)
    print("Columns in the dataset:", df.columns)
    
    relevant_column = 'HomeTeam' if is_home else 'AwayTeam'
    
    team_data = df[df[relevant_column] == team]
    
    if team_data.empty:
        raise ValueError(f"Team {team} not found in the dataset.")

    avg_goals = team_data['FTHG'].mean()  # Full-time home goals
    win_pct = (team_data['FTR'] == 'H').mean()  # Assuming 'H' stands for home win
    goal_diff = (team_data['FTHG'] - team_data['FTAG']).mean()  # Home goals - Away goals
    
    return avg_goals, win_pct, goal_diff

# Route for main page with team selection form
@app.route('/')
def index():
    return render_template('index.html', teams=teams)

@app.route('/predict', methods=['POST'])
def predict():
    # Get user-selected home and away teams
    home_team = request.form.get('home_team')
    away_team = request.form.get('away_team')
    
    # Encode team selections
    home_team_encoded = home_encoder.transform([home_team])[0]
    away_team_encoded = away_encoder.transform([away_team])[0]
    
    # Provide the correct path to your CSV file
    csv_file_path = "final_dataset.csv"
    
    # Get form stats for both home and away teams
    home_avg_goals, home_win_pct, home_goal_diff = get_team_form_stats(home_team, is_home=True, csv_file_path=csv_file_path)
    away_avg_goals, away_win_pct, away_goal_diff = get_team_form_stats(away_team, is_home=False, csv_file_path=csv_file_path)

    # Prepare features for the model's prediction (match the training features)
    features = np.array([[home_team_encoded, away_team_encoded, home_avg_goals, away_avg_goals,
                          home_win_pct, away_win_pct, home_goal_diff, away_goal_diff,
                          home_avg_goals, away_avg_goals, home_win_pct, away_win_pct,
                          home_goal_diff, away_goal_diff, 0, 0]])  # Example additional features if needed
    
    # Make prediction
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    # Map the prediction result to human-readable output
    result_map = {0: "Home Win", 1: "Draw", 2: "Away Win"}
    prediction_text = result_map.get(prediction, "Unknown Result")
    
    # Send back prediction, probabilities, and selected teams to display in the template
    return render_template(
        'index.html',
        teams=teams,
        selected_home_team=home_team,
        selected_away_team=away_team,
        prediction_text=prediction_text,
        home_win_prob=probabilities[0],
        draw_prob=probabilities[1],
        away_win_prob=probabilities[2]
    )

if __name__ == '__main__':
    app.run(debug=True)
