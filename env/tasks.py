import pandas as pd

def easy_data():
    data = {
        "age": [25, None, 30],
        "salary": [50000, 60000, None],
    }
    return pd.DataFrame(data)

def medium_data():
    data = {
        "age": [25, None, 30, 22],
        "salary": [50000, 60000, None, 52000],
        "city": ["NY", "LA", None, "NY"]
    }
    return pd.DataFrame(data)

def hard_data():
    data = {
        "age": [25, None, 30, 22, 22],
        "salary": [50000, 60000, None, 52000, 52000],
        "city": ["NY", "LA", "NY", None, "NY"]
    }
    return pd.DataFrame(data)
