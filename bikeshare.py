import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
        
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    Cities_available= ['chicago', 'new york city', 'washington']
    while True:
        city = input('Choose the city to analyse from chicago, new york city or washington \n').lower()
        if city in Cities_available:
            break
        else:
            print('Opps! you have entered an invalid city')
            


    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = ['jan', 'feb', 'mar','apr', 'may','jun']
    month_choice = input ('would you like to analyze all months? \n Please enter \"yes\" for all months and \"no\" for a specific month \n')
    if month_choice == 'yes':
        month = 'all'
    else:
        while True:
            month = input('Choose month \n Please input as short form e.g jan for January...\n').lower()
            if month in months_list:
                break
            else:
                print('Opps! you have entered an invalid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['sun','mon','tue','wed','thurs','fri','sat']
    day_choice= input ('would you like to analyze all days? \n Please enter \"yes\" for all days and \"no\" for a specific days \n')
    if day_choice =='yes':
        day = 'all'
    else:
        while True:
            day=input('Choose day \n Please input as short form e.g sun for sunday...\n').lower()
            if day in day_list:
                break
            else:
                print('Opps! you have entered an invalid day')

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
     #load csv data files
    df = pd.read_csv(CITY_DATA [city])
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #add column for Month, Day of week and Hour
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour
    
     #sort by month or by day as user demands
    month_index ={'jan':1, 'feb':2, 'mar':3,'apr':4, 'may':5,'jun':6}
    if month != 'all':
        df = df.loc[df['Month'] == month_index[month]]
        
    day_index = {'mon':0,'tue':1,'wed':2, 'thurs':3, 'fri':4, 'sat':5,'sun':6,}
    if day != 'all':
        df= df.loc[df['Day_of_Week'] == day_index[day]]  
       
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    
    print('The most common month is', most_common_month)
    
    #display the most common day of week
    most_common_weekday = df['Day_of_Week'].mode()[0]
    
    print('The most common day of the week is', most_common_weekday)
    #display the most common start hour
    
    most_common_starthour = df['Hour'].mode()[0]
    print('The most common common start hour is', most_common_starthour)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    most_widely_used_startstation=df['Start Station'].mode()[0]
    print ('The most widely used start station is', most_widely_used_startstation)


    #display most commonly used end station
    most_widely_use_endstation = df['End Station'].mode()[0]
    print ('The most widely used End station is', most_widely_use_endstation)


    #display most frequent combination of start station and end station trip
    freqcomb_startend = df['Start Station'] + " to " + df['End Station']
    freqcomb_startend = freqcomb_startend.mode()[0]
    print('The most often combined start station and end station trip is', freqcomb_startend)  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
 #Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("The count of user types from the data is: \n" + str(user_type_count))

    #Display counts of gender
    if 'Gender' in df.columns:
        gender_count= df['Gender'].value_counts()
        print("The count of gender from the data is: \n" + str(gender_count))
    else:
        print('Sorry! There is no available data for Gender')

    #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob= df['Birth Year'].min()
        print('The earliest birth year of users is \n', earliest_yob)
        most_recent_yob =df['Birth Year'].max()
        print('The most recent birth year of users is \n', most_recent_yob)
        most_common_yob =df['Birth Year'].mode()[0]
        print('The most common birth year of users is \n', most_recent_yob)
    else:
        print('Sorry! There is no available data for Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_raw_data(df):
    """Displays five rows of the raw data on user request """
    print(df.head())
    next = 0
    while True:
        show_raw_data = input('\n Want to view the next five row of raw data? Enter yes or no.\n')
        if show_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

  