import pandas as pd

def analyze_categorical_features(dataframe, columns):
    """
    Analyze unique values and their counts for specified columns in a DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to analyze.
    columns (list): List of column names to analyze.

    Returns:
    pd.DataFrame: A DataFrame with columns 'Column', 'Unique Values', and 'Unique Count'.
    """
    analysis_results = []
    for column in columns:
        unique_values = dataframe[column].unique()
        unique_count = dataframe[column].nunique()
        analysis_results.append({
            'Categorical Feature': column,
            'Unique Values': unique_values,
            'Unique Value Count': unique_count
        })
    result_df = pd.DataFrame(analysis_results)
    return result_df