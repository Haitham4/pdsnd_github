import pandas as pd
import datetime as dt
import calendar as cal
import time

city_list = ['chicago', 'new york city', 'washington', 'all']
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

# Get inputs from user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ''
    month = ''
    day = ''

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while city not in city_list:
        city = input("Please enter a name of a city to analyze\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in month_list:
        month = input("Please enter a name of a month (from January to June)\n").capitalize()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days_of_week:
        day = input("Please enter a week day to analyze (i.e Monday, Friday)\n").capitalize()

    print('-'*40)
    return city, month, day

# Load datasets into a dataframe
def load_data(city, month, day):

    cities = {
        'chicago': 'chicago.csv',
        'new york city': 'new_york_city.csv',
        'washington': 'washington.csv'
    }

    # Fetch the city based on the user's choice
    df = pd.read_csv(cities[city])

    # Convert dates to datetime objects
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['start_hour'] = df['Start Time'].dt.hour

    # Convert numerical months and week days to nominal ones
    df['month'] = df['Start Time'].dt.month.apply(lambda x: str(cal.month_name[x]))
    df['day_of_week'] = df['Start Time'].dt.day_name().apply(lambda x: str(x))

    # Apply filters if provided
    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print(df.shape)

    # TO DO: display the most common month
    print("The most common month for trips to be held is {}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week for a trip is {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common hour for a trip to start is {}".format(df['start_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("The most commonly used start and end station combination is \n{}".format(df[['Start Station', 'End Station']].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate travel time
    df['total_travel_time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time

    print("The total travelled time for all riders is {}".format(df['total_travel_time'].sum()))

    # TO DO: display mean travel time
    print("The average travel time is {}".format(df['total_travel_time'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts()
    print("Over all rides, there were {} Subscribers and {} Customers (non-subscribers)".format(counts.loc['Subscriber'],
                                                                                                counts.loc['Customer']))

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("{} of riders were males While {} were females".format(gender_counts.loc['Male'],
                                                                 gender_counts.loc['Female']))

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The oldest rider was born on {} while the youngest was born on {}. "
          "\nRiders who were born on {} were the most common among all riders based on birth year".format(
        int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

main()
