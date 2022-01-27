# load important libraries 
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs
    import sys
    count = 0
    while True:
        try:
            city = input('Would you like to see the data for Chicago, New York city, Washington?: ').strip().lower()
            if(city in ['washington', 'new york city', 'chicago']):
                break
            else: 
                print('Please choose from one of the cities, Chicago, New York city or Washington')
                continue
        except Exception as e: 
            print("Exception occurred: {}".format(e))
            print('Invalid Input. Try again.')
    print('Good job. You selected : ', city)

# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Input for month (all, January, February, ... , June : ').strip().lower()
            if(month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']):
                break
            else: 
                print('Please choose from one of the following months,', end=' ') 
                print('January, February, March, April, May, June or all')
                continue
        except Exception as e: 
            print("Exception occurred: {}".format(e))
            print('Invalid Input. Try again.')
    print('Good job. You selected : ', month)


# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Input for week, all, Monday, Tuesday, ... Sunday: ').strip().lower() 
            if(day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
                break
            else: 
                print('Please choose from one of the following days, Monday, Tuesday, Wednesday,\
                      Thursday, Friday, Saturday, Sunday or all')
                continue
        except Exception as e: 
            print("Exception occurred: {}".format(e))
            print('Invalid Input. Try again.')
    print('Good job. You selected : ', day)


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
    if (city != "all"): 
        df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'], format="%Y-%m-%d %H:%M:%S")
    df['End Time'] = pd.to_datetime(df['End Time'], format="%Y-%m-%d %H:%M:%S")
    
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if (month != "all"): 
        df = df[df['month'] == month]

    if (day != "all"): 
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.

    Args:
        (df) - Pandas DataFrame containing city data filtered by month and day
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\n#1 Calculating Popular Times (i.e., occurs most often in the Start Time)  of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common start hour
    print('What was the most common hour of the day?\n')
    print("Calculating statistic...")
    key = df['hour'].value_counts().idxmax()
    value = df['hour'].value_counts().max()
    print(key, value,"\n")

    if (month == "all"): 
        print("Calculating Most Common Month statistic...")
        key = df['month'].value_counts().idxmax()
        value = df['month'].value_counts().max()
        print(key, value,"\n")

    if (day == "all"): 
        print("Calculating Most Common Day of Week statistic...")
        key = df['day_of_week'].value_counts().idxmax()
        value = df['day_of_week'].value_counts().max()
        print(key, value,"\n")

    print('What was the most popular trip from start to end?\n')
    print("Calculating statistic...")
    
    key = df['Start Station'].value_counts().idxmax()
    value = df['Start Station'].value_counts().max()
    print(key, value, "\n")

    key1 = df['End Station'].value_counts().idxmin()
    value1 = df['End Station'].value_counts().min()
    print(key1, value1, "\n")

    print("What is the breakdown of users?") 
    print("Calculating statistic...")
    key = df['User Type'].value_counts().idxmax()
    value = df['User Type'].value_counts().max()
    print(key, value)

    key = df['User Type'].value_counts().idxmin()
    value = df['User Type'].value_counts().min()
    print(key, value, "\n")

    #display the most common day of week

    if (day  == "all"): 
        print("Most common day of week")
        print("Calculating statistic...")
        key = df['day_of_week'].value_counts().idxmax()
        value = df['day_of_week'].value_counts().max()
        print(key, value,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """
    #2 Displays statistics on the most popular stations and trip.

    Args:
        (df) - Pandas DataFrame containing city data filtered by month and day
    """

    print('\n#2: Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print("Commonly used start station")
    print("Calculating statistic...")
    keys = df['Start Station'].value_counts().idxmax()
    values = df['Start Station'].value_counts().max()
    print(keys, values,"\n")

    #Display most commonly used end station
    print("Commonly used End station")
    print("Calculating statistic...")
    keye = df['End Station'].value_counts().idxmax()
    valuee = df['End Station'].value_counts().max()
    print(keye, valuee,"\n")

    #Display most commonly used end station
    groups = df.groupby(['Start Station','End Station'])
    print('Most common trip from start to end (ie most frequent combination of start and end stations')
    print("Calculating statistic...")
    print(groups.size().sort_values(ascending=False).reset_index(name='Count').head(1))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (df) - Pandas DataFrame containing city data filtered by month and day
    """

    print('\n#3: Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time") 
    print("Calculating statistic...")
    print(df['Trip Duration'].sum())
    print("Count") 
    print(df['Trip Duration'].count(),"\n")
    print("Average travel time") 
    print("Calculating statistic...")
    print(df['Trip Duration'].mean(),"\n")
    
    # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users

    Args:
        (df) - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyze
    """

    print('\n#4: Calculating User Info Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("What is the breakdown of users?") 
    print("Calculating statistic...")
    key = df['User Type'].value_counts().idxmax()
    value = df['User Type'].value_counts().max()
    print(key, value)

    key = df['User Type'].value_counts().idxmin()
    value = df['User Type'].value_counts().min()
    print(key, value,"\n")

    # Washington city doesnt have 'Gender' and 'Birth Year'
    print("What is the breakdown of Gender?") 
    print("Calculating statistic...")
    if (city != 'washington'):
        key = df['Gender'].value_counts().idxmax()
        value = df['Gender'].value_counts().max()
        print(key, value)
        key = df['Gender'].value_counts().idxmin()
        value = df['Gender'].value_counts().min()
        print(key, value,"\n")

        # Display earliest, most recent, and most common year of birth
        print("Most Recent year of birth")
        print(df['Birth Year'].max().astype(int))

        print("Earliest year of birth")
        print(df['Birth Year'].min().astype(int))

        print("Most common year of birth")
        temp = df['Birth Year'].mode().astype(int)
        print(temp[0],"\n")

    else: 
        print('No Gender data to share')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        # get the city, name and day 
        city, month, day = get_filters()
        print("Calculating statistic...")

        # Load the data 
        df = load_data(city, month, day)

        # code block to view the first 5 lines of the data
        view_logic = True
        # vs: view start index; ve: view ending index
        vs = 0
        ve = 5
        nrow_max = df.shape[0]
        ncount = 5
        while view_logic:
            try:
                view_ans = input('Would you like to view the top 5 lines of the dataset? Enter yes or no: ').strip().lower()
                if(view_ans in ['yes', 'no']):
                     if view_ans == 'yes': 
                          if ve > nrow_max: 
                              print("We are at the end of the file, here are the last few lines")
                              print(df.iloc[vs:nrow_max])
                              break
                          else: 
                              print(df.iloc[vs:ve])
                              vs += 5
                              ve += 5
                              continue
                     else: 
                          print("Thank you for choosing no to skip viewing the top 5 lines of the dataset")
                          break
                else: 
                    print('Please choose from one of the following choices, yes or no')
                    continue
            except Exception as e: 
                print("Exception occurred: {}".format(e))
                print('Invalid Input. Try again.')

        # time stat
        time_stats(df, month, day)


        # calculate popular station
        station_stats(df)

        # calculate trip duration
        trip_duration_stats(df)
        
        # calculate popular trip
        user_stats(df, city)

        # ask user input whether they want to restart or not
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

