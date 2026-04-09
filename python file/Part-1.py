
import pandas as pd

# Create dataset using dictionary
data = {
    "Name": ["Alem", "Bekele", "Chala", "Dawit", "Eden",
             "Fikir", "Genet", "Hana", "Ibrahim", "Jemal",
             "Kebede", "Liya", "Marta", "Nati", "Omar"],

    "Age": [20, 21, 19, 22, 20,
            23, 21, 20, 22, 19,
            24, 20, 21, 23, 22],

    "Department": ["CS", "IT", "CS", "SE", "IT",
                   "CS", "SE", "IT", "CS", "SE",
                   "IT", "CS", "SE", "IT", "CS"],

    "GPA": [3.5, 3.2, 3.8, 2.9, 3.0,
            3.6, 2.8, 3.1, 3.7, 2.7,
            3.3, 3.9, 2.6, 3.4, 3.8],

    "Graduated": ["Yes", "No", "Yes", "No", "Yes",
                  "Yes", "No", "Yes", "Yes", "No",
                  "Yes", "Yes", "No", "Yes", "Yes"]
}

# Create custom index
index_labels = [f"Std{i}" for i in range(1, 16)]

# Create DataFrame
df = pd.DataFrame(data, index=index_labels)

# Display DataFrame
df
