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
    try:
        city = input("Enter name of city [chicago,new york city,washington]:")
        while city not in ['chicago', 'new york city', 'washington']:
            print("Not analysed Enter city again")
            city = input("Enter city [chicago,new york city,washington]: ")

        month = input("Enter month name: ").lower()
        while month not in['january','february','march','april','may','june','all']:
            print("Not analysed Enter month again")
            month = input("Enter month: ").lower()


        day = input("enter day of week in lower case: ").lower()
        while day not in['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            print("Not analysed Enter day again")
            day = input("Enter day: ").lower()
        print('-' * 40)
        return city, month, day
    except Exception as e:
        print('An error with your inputs occured: {}'.format(e))

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    try:
        df['month'] = df['Start Time'].dt.month
        print("most common month: {}".format(df['month'].mode()[0]))
    except Exception as e:
        print('Couldn\'t calculate the most common day of week, as an Error occurred: {}'.format(e))

    try:
        df['day_of_week'] = df['Start Time'].dt.day
        print("most common day of week: {}".format(df['day_of_week'].mode()[0]))
    except Exception as e:
        print('Couldn\'t calculate the most common day of week, as an Error occurred: {}'.format(e))

    try:
        df['hour'] = df['Start Time'].dt.hour
        print("most common start hour: {}".format(df['hour'].mode()[0]))
    except Exception as e:
        print('Couldn\'t calculate the most common day of week, as an Error occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("most common used start station: {}".format(df['Start Station'].mode()[0]))

    print("most common used end station: {}".format(df['End Station'].mode()[0]))

    df['Trip'] = df['Start Station'] + " " + df['End Station']

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        print("Total Travel Time: {}".format(df['Trip Duration'].sum()))
    except Exception as e:
        print('Couldn\'t calculate the total travel time of users, as an Error occurred: {}'.format(e))
    try:
        print("Mean Travel Time: {}".format(df['Trip Duration'].mean()))
    except Exception as e:
        print('Couldn\'t calculate the total travel time of users, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        print("Count of user types: {}".format(int(df['User Types'].value_counts)))
    except Exception as e:
        print('Couldn\'t calculate the type of users, as an Error occurred: {}'.format(e))
    try:
        print("Count of Gender: {}".format(df['Gender'].value_counts))
    except Exception as e:
        print('Couldn\'t calculate the amount and gender of users, as an Error occurred: {}'.format(e))
    try:
        print("Oldest birth year: {}".format(df['Birth Year'].min()))
        print("Youngest birth year: {}".format(df['Birth Year'].max()))
        print("Most recent birth year: {}".format(df['Birth Year'].mode()))
    except Exception as e:
        print('Couldn\'t calculate the age structure of our customers, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main() -> object:
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
