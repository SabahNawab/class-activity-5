import numpy as np
import pandas as pd


class LR():
    def __init__(self):
        self.tw = None  
        
    
    def linear_regression_hypothesis(self, x_values, slope_intercept_values):
        
        x_values_with_bias = np.column_stack((x_values, np.ones((x_values.shape[0], 1))))
        return np.matmul(x_values_with_bias, slope_intercept_values.reshape(-1, 1))
    
    
    def loss_func(self, slope_intercept_values, out_predicts, x_values):
        predictions = self.linear_regression_hypothesis(x_values, slope_intercept_values)
        return np.mean(np.power((out_predicts - predictions), 2))  
    
    
    def partial_derivative(self, x_values, out_predicts, slope_intercept_values):
        predictions = self.linear_regression_hypothesis(x_values, slope_intercept_values).flatten()  
        errors = out_predicts - predictions  
       
        derivative = -2 * np.mean(errors[:, np.newaxis] * np.column_stack((x_values, np.ones((x_values.shape[0], 1)))), axis=0)
        return derivative

    
    def gradient_descent_fun(self, learning_rate, derivative, slope_intercept_values):
        return slope_intercept_values - learning_rate * derivative  
    
    def train(self, x_values, out_predicts, learning_rate=0.01, epochs=10, loss_after_epochs=5):
        
        w = np.random.uniform(-1, 1, x_values.shape[1] + 1)  
        
        
        for i in range(epochs):
            outputs = self.linear_regression_hypothesis(x_values, w)  
            derivative = self.partial_derivative(x_values, out_predicts, w)  
            w = self.gradient_descent_fun(learning_rate, derivative, w)  
            loss = self.loss_func(w, out_predicts, x_values)  
            
            
            if i % loss_after_epochs == 0:
                print(f"Epoch {i}, LOSS = {loss}")
        
        
        self.tw = w
        return w
    
   
    def predict(self, x_value):
        predictions = self.linear_regression_hypothesis(x_value, self.tw)
        
        return np.maximum(predictions, 0)
    
    
    def get_weights(self):
        return self.tw

def Load_AND_Preprocess(path):
    df = pd.read_csv(path)
   
    df = pd.get_dummies(df, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'], drop_first=True)

    X = df.drop('price', axis=1).values  
    y = df['price'].values  


    min_x = np.min(X, axis=0)
    max_x = np.max(X, axis=0)
    scaled_data_x = (X - min_x) / (max_x - min_x)

    min_y = np.min(y)
    max_y = np.max(y)
    scaled_data_y = (y - min_y) / (max_y - min_y)
    return scaled_data_x,scaled_data_y,min_y,max_y
    

def trainning():
    path=r"D:\Housing.csv"
    scaled_data_x,scaled_data_y,min_y,max_y=Load_AND_Preprocess(path)
    model = LR()
    model.train(scaled_data_x, scaled_data_y, learning_rate=0.001, epochs=1000, loss_after_epochs=100)


    predictions = model.predict(scaled_data_x)


    predictions_up = predictions * (max_y - min_y) + min_y
    print("Predictions: ", predictions_up)
if __name__ == '__main__':
    trainning()