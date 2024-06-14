import numpy as np
import pandas as pd

def generate_new_data(num_samples):
    # Define coefficients for each feature
    coefficients = {
        'area': 2268,
        'bedrooms': 3000,
        'bathrooms': 2000,
        'stories': 1500,
        'mainroad': 5000,
        'guestroom': 3000,
        'basement': 2000,
        'hotwaterheating': 1000,
        'airconditioning': 4000,
        'parking': 2500,
        'prefarea': 3500
    }

    # Define encoding for furnishing status
    furnishing_encoding = {
        'furnished': 1,
        'semi-furnished': 0.5,
        'unfurnished': 0
    }

    # Generate new independent variables (features)
    new_data = {}
    for feature, coeff in coefficients.items():
        if feature == 'furnishingstatus':
            new_data[feature] = np.random.choice(list(furnishing_encoding.keys()), num_samples)
        elif feature == 'area':
            new_data[feature] = np.random.choice(1,5000,num_samples)
        elif feature in ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']:
            new_data[feature] = np.random.choice(['yes', 'no'], num_samples)
        else:
            new_data[feature] = np.random.randint(0, 5, num_samples)  # Adjust range based on feature

    # Generate new dependent variable (price) based on the coefficients and features
    new_data['price'] = sum(new_data[feature] * coeff for feature, coeff in coefficients.items() if feature != ['furnishingstatus','mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea'])

    return pd.DataFrame(new_data)

def add_new_data(file_path, num_iterations):
    # Read the existing CSV file into a DataFrame
    existing_data = pd.read_csv(file_path)

    # Append new data to the existing DataFrame
    for _ in range(num_iterations):
        new_data = generate_new_data(num_samples=100)  # Define the number of samples for each new data
        existing_data = existing_data.append(new_data, ignore_index=True)

    # Write the updated DataFrame back to the CSV file
    existing_data.to_csv(file_path, index=False)

    print("New data has been added to the existing CSV file.")

# Example usage
file_path = r'C:\Users\OS\Desktop\Workspace\hapt\Housing.csv'  # Replace 'path_to_your_existing_file.csv' with the actual file path
num_iterations = 5  # Number of times to generate and add new data
add_new_data(file_path, num_iterations)
