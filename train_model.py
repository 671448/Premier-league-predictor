import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# Load and preprocess the dataset
df = pd.read_csv('final_dataset.csv')

# Encode categorical columns
encoder_home = LabelEncoder()
encoder_away = LabelEncoder()
encoder_ftr = LabelEncoder()

df['HomeTeam'] = encoder_home.fit_transform(df['HomeTeam'])
df['AwayTeam'] = encoder_away.fit_transform(df['AwayTeam'])
df['FTR'] = encoder_ftr.fit_transform(df['FTR'])

# Aggregate home and away stats
home_team_stats = df.groupby('HomeTeam').agg({'FTHG': 'mean', 'FTAG': 'mean'}).reset_index()
away_team_stats = df.groupby('AwayTeam').agg({'FTHG': 'mean', 'FTAG': 'mean'}).reset_index()
home_team_stats.columns = ['HomeTeam', 'HomeGoalsAvg', 'AwayGoalsAvg']
away_team_stats.columns = ['AwayTeam', 'HomeGoalsAvg_Away', 'AwayGoalsAvg_Away']

# Merge stats with main dataframe
df = pd.merge(df, home_team_stats, on='HomeTeam', how='left')
df = pd.merge(df, away_team_stats, on='AwayTeam', how='left')

# Function to calculate form metrics
def calculate_form_metrics(team, is_home=True):
    df_team = df[df['HomeTeam'] == team] if is_home else df[df['AwayTeam'] == team]
    df_team = df_team.tail(5)  # Last 5 matches for form metrics
    
    avg_goals = df_team['FTHG' if is_home else 'FTAG'].mean()
    win_percentage = (df_team['FTR'] == ('H' if is_home else 'A')).sum() / len(df_team) * 100
    goal_diff = (df_team['FTHG' if is_home else 'FTAG'] - df_team['FTAG' if is_home else 'FTHG']).mean()
    
    return avg_goals, win_percentage, goal_diff

# Adding form metrics to the DataFrame
df['HomeAvgGoals'] = df['HomeTeam'].apply(lambda x: calculate_form_metrics(x, True)[0])
df['AwayAvgGoals'] = df['AwayTeam'].apply(lambda x: calculate_form_metrics(x, False)[0])
df['HomeWinPercentage'] = df['HomeTeam'].apply(lambda x: calculate_form_metrics(x, True)[1])
df['AwayWinPercentage'] = df['AwayTeam'].apply(lambda x: calculate_form_metrics(x, False)[1])
df['HomeGoalDiff'] = df['HomeTeam'].apply(lambda x: calculate_form_metrics(x, True)[2])
df['AwayGoalDiff'] = df['AwayTeam'].apply(lambda x: calculate_form_metrics(x, False)[2])

# Head-to-head stats function
def head_to_head_stats(home_team, away_team):
    home_head_to_head = df[(df['HomeTeam'] == home_team) & (df['AwayTeam'] == away_team)]
    away_head_to_head = df[(df['HomeTeam'] == away_team) & (df['AwayTeam'] == home_team)]
    home_wins = (home_head_to_head['FTR'] == 'H').sum()
    away_wins = (away_head_to_head['FTR'] == 'A').sum()
    return home_wins, away_wins

df['HomeVsAwayWins'], df['AwayVsHomeWins'] = zip(*df.apply(lambda row: head_to_head_stats(row['HomeTeam'], row['AwayTeam']), axis=1))

# Prepare features and target variable
X = df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HomeGoalsAvg', 'AwayGoalsAvg', 
        'HomeGoalsAvg_Away', 'AwayGoalsAvg_Away', 'HomeAvgGoals', 'AwayAvgGoals', 
        'HomeWinPercentage', 'AwayWinPercentage', 'HomeGoalDiff', 'AwayGoalDiff', 
        'HomeVsAwayWins', 'AwayVsHomeWins']]
y = df['FTR']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class_weights = {0: 1, 1: 0.5, 2: 1}

# Set up Random Forest with GridSearch and custom class weights
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'class_weight': [class_weights]  # Adding class weights here
}
grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Save the model
with open('rf_model.pkl', 'wb') as file:
    pickle.dump(grid_search.best_estimator_, file)

# Evaluate the model
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))