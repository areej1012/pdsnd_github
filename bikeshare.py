import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES=  ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    day=""
    month=""
    while True:
        city = input('Would you see data for chicago, new york city or washington ? \n ').lower()
        if city in CITIES:
            break
            
    filter_by= input('Would like filter the date by month, day, both or not \n ').lower()
    if filter_by == "both":
        # TO DO: get user input for month (all, january, february, ... , june)
        month= input('What month do you choose? like march \n ').lower()
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('which day ? please write the name of the day like is : Sunday. \n').lower()
    elif filter_by == "month":
        month= input('What month do you choose? like march \n ').lower()
    elif filter_by == "day":
        day = input('which day ? please write the name of the day like is : Sunday. \n').lower()
    else:
        day=""
        month=""
      
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    # if the month and day are not empty then load data based on them
    if month !="" and day !="":
        df['month'] = df['Start Time'].dt.month
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        df = df[df['month'] == month]
        df['day_of_week'] = df['Start Time'].dt.weekday_name    
        df = df[df['day_of_week'] == day.title()]
    elif month != "":
        df['month'] = df['Start Time'].dt.month
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        df = df[df['month'] == month]
        df['day_of_week'] = df['Start Time'].dt.weekday_name  
    elif day !="":
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name    
        df = df[df['day_of_week'] == day.title()]
    else:
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name    
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
     # extract hour from the Start Time column to create an hour column
    
    # TO DO: display the most common month
    #mod method Most Frequent Values
    common_month=df['month'].mode()[0]
    print("most common month:", common_month)
    
    # TO DO: display the most common day of week
    comm_day_of_week=df['day_of_week'].mode()[0]
    print("most common day of week:" , comm_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    count_start_s=df['Start Station'].value_counts()
    count_end_s = df['End Station'].value_counts()
    print("Popular Start Station:", popular_start_station)
    
    # TO DO: display most commonly used end station
    print("Popular End Station:", popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station= df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Popular Start and End Station:", popular_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print("total Duration: {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    Avg_travel_time= df['Trip Duration'].mean()
    print("Avg Duration: {} seconds".format(round(Avg_travel_time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    for index, user_count in enumerate(user_types):
        print("  {}: {}".format(user_types.index[index], user_count))


    # TO DO: Display counts of gender
    # check if df have columns called Gander or Birth years
    if 'Gender' in df.columns:
        print("\n count of gander")
        gender_counts = df['Gender'].value_counts()
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print("\nThe most earliest birth year:", int(earliest_year))
        recent_year = df['Birth Year'].max()
        print("The most recent year:", int(recent_year))
        #This ref help me: 
        #https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column/48590361
        common_year =  df['Birth Year'].value_counts().idxmax()
        print("The common year:", int(common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Ask user if he/she is wants display raw data"""
    i = 0
    raw = input("Would you like to view individual trip data? yes or no?\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)
    
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i: i + 5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw =input("\nWould you like to view individual trip data? yes or no?\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
