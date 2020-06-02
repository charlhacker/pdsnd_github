# FINAL CODE FOR UDACITY PYTHON ASSIGNMENT

import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','washington','new york city']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
even_more = ' '

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Hello! Let\'s explore some US bikeshare data! \n Which city would you like to learn about: Chicago, New York City, or Washington?')

    while True:
        city = input('Enter city: ').lower()
        if city in cities:
            break
        else:
            print('Oops, invalid input. Please enter one of the three cities shown above.')

        # TO DO: get user input for month (all, january, february, ... , june)

    print('OK. We\'ll look at {}. Enter the month you would like to see data for, or enter "all" if you don\'t want to filter by month'.format(city))

    while True:
        month = input('Enter month: ').lower()
        if month in months:
            break
        else:
            print('Oops, invalid input. We only have data for the months January through to June. Please enter one of these or enter "all" to see data for all months.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('OK. Enter the day you would like to see data for, or enter "all" if you don\'t want to filter by day.'.format(month,city))

    while True:
        day = input('Enter day of week: ').lower()
        if day in days:
            break
        else:
            print('Oops, invalid input. Please enter a specific day of the week or ''all''.')

    print('OK! Let\'s look at data for the following: \n City: {} \n Month: {} \n Day of Week: {} \n'.format(city,month,day))
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
# load data file into a dataframe
    df = pd.read_csv(city_data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['combo'] = df['Start Time'].dt.hour
    df['combo_station'] = df['Start Station'] + ' to ' + df['End Station']

    # filter by month if applicable
    if month != 'all': #if month is specific, then assign month number to input
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is {}.'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is {}.'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour for trips is {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most popular start station is {}.'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular end station is {}.'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = df['combo_station'].mode()[0]
    print('The most frequent combination of start and end station trip is from {}.'.format(popular_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # NB. Trip durations coverted from seconds to minutes.

    # TO DO: display total travel time
    total_duration = (int(df['Trip Duration'].sum())) // 60
    print('Total travel time was approx. {} minutes.'.format(total_duration))

    # TO DO: display mean travel time
    mean_duration = (int(df['Trip Duration'].mean())) // 60
    print('Average travel time was approx. {} minutes.'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User types were as follows: {}.'.format(user_type))

    # TO DO: Display counts of gender
    gender_type = df['Gender'].value_counts()
    print('Gender split was as follows {}.'.format(gender_type))

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest_birth = int(df['Birth Year'].min())
    print('The oldest customer was born in {}.'.format(oldest_birth))

    youngest_birth = int(df['Birth Year'].max())
    print('The youngest customer was born in {}.'.format(youngest_birth))

    popular_birth = int(df['Birth Year'].mode()[0])
    print('The most popular birth year was {}.'.format(popular_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            see_more = input('Would you like to see a preview of the raw data?\n').lower()
            if see_more == 'yes':
                print(df.head(5))
            elif see_more == 'no':
                break
            else:
                print('Invalid input - please enter yes or no.')

            while see_more == 'yes':
                even_more = input('Would you like to see more raw data?\n').lower()
                if even_more == 'yes':
                    num_rows = input('How many rows?')
                    print(df.head(int(num_rows)))
                elif even_more == 'no':
                    restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
                    if restart == 'no':
                        exit()
                    elif restart == 'yes': #NB needs a fix - loops back to preview rather than program restart
                        break
                    else:
                        print('Invalid input - please enter yes or no.')
                else:
                    print('Invalid input - please enter yes or no.')

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart == 'no':
                exit()
            if restart == 'yes':
                break
            else:
                print('Invalid input - please enter yes or no.')


if __name__ == "__main__":
            main()
