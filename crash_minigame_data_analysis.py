import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


class CrashGameDataAnalysis:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def analyze_data(self):
        # Calculate average crash multiplier, average cash out multiplier, and win rate
        avg_crash_multiplier = self.data['crash_multiplier'].mean()
        avg_cash_out_multiplier = self.data['cash_out_multiplier'].mean()
        win_rate = self.data['outcome'].mean()

        print(f'Average crash multiplier: {avg_crash_multiplier}')
        print(f'Average cash out multiplier: {avg_cash_out_multiplier}')
        print(f'Win rate: {win_rate}')

    def visualize_data(self):
        # Plot histograms of crash multipliers and cash out multipliers
        plt.hist(self.data['crash_multiplier'], bins=20, alpha=0.5, label='Crash Multiplier')
        plt.hist(self.data['cash_out_multiplier'], bins=20, alpha=0.5, label='Cash Out Multiplier')
        plt.legend(loc='upper right')
        plt.show()

    def predict_future(self):
        # Use linear regression to predict crash multiplier
        X = self.data.index.values.reshape(-1, 1)
        y = self.data['crash_multiplier']
        model = LinearRegression().fit(X, y)

        # Predict the crash multiplier for the next game
        next_game = np.array([len(self.data)]).reshape(-1, 1)
        predicted_crash_multiplier = model.predict(next_game)

        print(f'Predicted crash multiplier for next game: {predicted_crash_multiplier[0]}')
