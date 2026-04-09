# Data Analysis Project: Foundation & Titanic Dataset

## Overview
This project demonstrates foundational data handling and real-world analysis in Python using pandas. It is divided into two parts:

- **Part 1:** Build your own dataset using a dictionary and perform basic exploration.  
- **Part 2:** Analyze the real Titanic dataset (`train.csv`) to extract meaningful insights about passenger survival.

The goal is to practice **data creation, cleaning, aggregation, and analysis**, and draw conclusions based on patterns in the data.

---

## Part 1: Create Your Own Dataset (Foundation)

### Task
- Build a pandas DataFrame from a dictionary of your choice.
- The dataset must include:
  - 5 columns (features)
  - 15 rows
  - Custom index

### Objectives
- Practice creating structured datasets manually.  
- Explore the dataset using basic methods.  
- Apply simple aggregation and filtering operations.

### Steps
1. Create a dictionary with 5 keys (columns) and 15 values per key (rows).  
2. Convert the dictionary into a pandas DataFrame with a custom index.  
3. Explore data using:
   - `.head()`, `.info()`, `.describe()`  
4. Handle missing or inconsistent data if present.  
5. Analyze the dataset with:
   - `groupby()` to compute statistics like averages or counts  
   - Filtering rows based on conditions  

### Example Insights
- Identify which categories or columns have higher values.  
- Understand distributions of numeric columns.  
- Practice summarizing key statistics.

---

## Part 2: Titanic Real Dataset Analysis

### Dataset
The Titanic dataset (`train.csv`) contains ~891 passengers with features including:

- `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`.

### Objectives
- Explore the dataset.  
- Clean missing values and remove irrelevant columns.  
- Analyze survival patterns using pandas.  
- Filter data for specific insights (gender, age, class).  

### Steps

1. **Data Exploration**
   - Inspect the dataset with `.head()`, `.info()`, `.describe()`.  
   - Identify missing values and duplicates.

2. **Data Cleaning**
   - Fill missing `Age` values with median.  
   - Fill missing `Embarked` values with mode.  
   - Drop `Cabin` due to many missing values.  
   - Remove duplicates.

3. **Data Analysis**
   - Compute survival rates by `Sex` (gender) and `Pclass` (class).  
   - Calculate average age per class.  
   - Segment passengers into age groups: Child, Teen, Adult, Senior.  
   - Compute survival rate per age group.

4. **Filtering**
   - Female passengers who survived.  
   - Children who survived.  
   - Passengers in 1st class with high survival probability.

5. **Insights**
   - Females had a higher survival rate than males.  
   - 1st class passengers had higher survival rates than 2nd and 3rd class.  
   - Children were prioritized, showing higher survival than adults.  
   - Female children in 1st class had the **highest survival probability**.

---

## Tools Used
- **Python 3**  
- **Pandas** for data handling and analysis  
- **Google Colab** for cloud-based execution and reproducibility  

---

## Conclusion
This project shows how **data creation, cleaning, and analysis** can reveal patterns and insights:

- Part 1 strengthens foundational skills by manually creating a dataset.  
- Part 2 demonstrates real-world application using the Titanic dataset, uncovering factors affecting survival.  
- Pandas provides an efficient, clean, and powerful way to explore and summarize datasets.