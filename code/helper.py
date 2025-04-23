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

def get_human_readable_names():
    """
    Returns a dictionary mapping feature names to human-readable names.

    Returns:
    dict: A dictionary where keys are feature names and values are human-readable names.
    """
    return {
        'adr': 'Average Daily Rate',
        'lead_time': 'Lead Time (Days)',
        'stays_in_weekend_nights': 'Weekend Stays (Nights)',
        'stays_in_week_nights': 'Weekday Stays (Nights)',
        'adults': 'Number of Adults',
        'children': 'Number of Children',
        'babies': 'Number of Babies',
        'previous_cancellations': 'Previous Cancellations',
        'previous_bookings_not_canceled': 'Previous Non-Canceled Bookings',
        'booking_changes': 'Booking Changes',
        'days_in_waiting_list': 'Days in Waiting List',
        'required_car_parking_spaces': 'Car Parking Spaces',
        'total_of_special_requests': 'Special Requests',
        'is_repeated_guest': 'Is Repeated Guest',
        'hotel_type': 'Hotel Type',
        'is_canceled': 'Booking Canceled',
        'arrival_date_year': 'Arrival Year',
        'arrival_date_month': 'Arrival Month',
        'arrival_date_week_number': 'Arrival Week Number',
        'arrival_date_day_of_month': 'Arrival Day of Month',
        'meal': 'Meal Plan',
        'country': 'Country',
        'market_segment': 'Market Segment',
        'distribution_channel': 'Distribution Channel',
        'reserved_room_type': 'Reserved Room Type',
        'assigned_room_type': 'Assigned Room Type',
        'deposit_type': 'Deposit Type',
        'customer_type': 'Customer Type',
        'reservation_status': 'Reservation Status',
        'reservation_status_date': 'Last Reservation Status Change Date',
        'agent': 'Agent',
        'company': 'Company'
    }

def categorize_guest(row):
    if row['adults'] == 1 and (row['children'] == 0 and row['babies'] == 0):
        return 'Solo Traveler'
    elif row['adults'] == 2 and (row['children'] == 0 and row['babies'] == 0):
        return 'Likely Couple'
    elif row['adults'] > 2 and (row['children'] == 0 and row['babies'] == 0):
        return 'Group of Adults'
    elif row['adults'] > 0 and (row['children'] > 0 or row['babies'] > 0):
        return 'Likely Family(s)'
    else:
        return 'Minors Only'

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    else:
        return 'Unknown'

def categorize_stay(row):
    if row['stays_in_weekend_nights'] > 0 and row['stays_in_week_nights'] == 0:
        return 'Weekend Only'
    elif row['stays_in_weekend_nights'] == 0 and row['stays_in_week_nights'] > 0:
        return 'Weekday Only'
    elif row['stays_in_weekend_nights'] > 0 and row['stays_in_week_nights'] > 0:
        return 'Both Weekend/Weekday'
    else:
        return 'No Stay'