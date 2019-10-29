import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york city','washington']

MONTHS = ['all','january', 'february','march','april','may','june']

DAYS = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('welcome to  US bikeshare data!'"\nLet's explore some US Bikeshare data!\n")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nChoose one of the cities: \n'
                     '\nChicago, New York City, Washington\n'
                     '\nI choose: ').lower()
        if city in CITIES:
            break
        else:
            print("\nPlease choose a city name from the list above!\n"
                  "\nLet's try again!\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nChoose a month: \n'
                      '\nJanuary, February, March, April,\nMay, June, or All\n\nI choose: ').lower()
        if month in MONTHS:
            break
        else:
            print("\nPlease choose a month name from the list above!\n"
                  "\nLet's try again! \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nChoose a day: \n'
                   '\nMonday, Tuesday, Wednesday, Thursday\nFriday, Saturday, Sunday, or All.\n\nI choose: ').lower()
        if day in DAYS:
            break
        else:
            print("\nPlease choose a day name from the above list!\n"
                  "\nLet's try again!")


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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month']= df['Start Time'].dt.month
    df['Week_Day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = MONTHS.index(month)
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Week_Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    the_most_common_month = df['Month'].mode()[0]
    print('The most common month: \n',
          MONTHS[the_most_common_month].title())



    # display the most common Week Day
    the_most_common_week_day = df['Week_Day'].mode()[0]
    print('The most common week day: \n',
          the_most_common_week_day)

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    the_most_common_start_hour = df['Hour'].mode()[0]
    print('\nthe most common start hour:\n',
          the_most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display the most commonly used start station
    the_most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station: \n' , the_most_commonly_used_start_station)

    # display the most commonly used end station
    the_most_commonly_used_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station: \n' , the_most_commonly_used_end_station)


    # display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep = ' To ')
    the_most_frequent_combination_of_start_to_end_trip = df['Start_End'].mode()[0]

    print('\nThe most frequent combination of start to end trip: \n', the_most_frequent_combination_of_start_to_end_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time: \n',
          round(sum(df['Trip Duration']),2), 'sec or,\n',
          round(sum(df['Trip Duration'])/60,2), 'min or,\n',
          round(sum(df['Trip Duration'])/3600,2), 'hr or,\n',
          round(sum(df['Trip Duration'])/86400,2), 'days.\n')

    # display mean travel time
    print('Mean Travel Time: \n',
          round(df['Trip Duration'].mean(),2), 'sec or,\n',
          round(df['Trip Duration'].mean()/60,2), 'min or,\n',
          round(df['Trip Duration'].mean()/3600,2), 'hr.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Types: \n', df['User Type'].value_counts())

    # Display counts of gender
    print('\nGender count: \n')
    try:
        print(df['Gender'].value_counts())
    except:
        print("No Gender data." )

    # Display earliest, most recent, and most common year of birth
    print('\nYear of birth stats: \n')
    try:
        print('\nThe earliest year of birth: \n', df['Birth Year'].min())
        print('\nThe most recent year of birth: \n', df['Birth Year'].max())
        print('\nThe most common year of birth: \n', df['Birth Year'].mode()[0])

    except:
        print("No Birth Year data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Display_Data(df):
    """Dis[lay more data of user"""
    for i in range(0, df.shape[0], 15):
        print('\n to show more data:\n')
        display = input("type 'yes' to display the next 15 lines of data, or 'no' to stop: ")
        if display.lower() != 'yes':
           break
        else:
           print(df.iloc[i: i + 15])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Display_Data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
