import time
import pandas as pd
from IPython.display import display

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    while True:
        try:
            city = (input('Would you like to see data for Chicago, New York, or Washington?\n')).casefold()
            df = pd.read_csv(CITY_DATA[city])
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            month = (input('Which month - January, February, March, April, May, June or all?\n')).casefold()
            df['month'] = df['Start Time'].dt.month
            df['day_of_week'] = df['Start Time'].dt.day_name()
            if month != 'all':
        # use the index of the months list to get the corresponding int
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = (months.index(month)) + 1
            df['month'].mode()[0]
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n').casefold()

            if day != 'all':
        # filter by day of week to create the new dataframe
                df = df[df['day_of_week'] == day.title()]

            break

        except Exception as e:

            print("{} is not a valid input, please provide an input from the given options only!".format(e))


    return city, month, day


    print('-'*120)





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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
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

     # display the most common month

    try:
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        common_month = df['month'].mode()[0]
        print('Most common month is:', months[common_month - 1])
    except Exception as e:
        print('Exception occurred while attempting to calculate most common month, please make sure you provide correct input option')
        print('Error details: {}'.format(e))

    # display the most common day of week
    try:
        common_weekday = df['day_of_week'].mode()[0]
        print('Most common day of week:', common_weekday)
    except Exception as e:
        print('Exception occurred while attempting to calculate most common day of week, please make sure you provide correct input option')
        print('Error details: {}'.format(e))


    # display the most common start hour
    try:
        df['hour'] = df['Start Time'].dt.hour

        # find the most popular hour
        popular_hour = df['hour'].mode()[0]
        print('Most Popular Start Hour:', popular_hour)
        print()

    except Exception as e:
        print('Error occurred while attempting to calculate most popular start hour, please make sure you provide a correct input option')
        print('Error details: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    try:
    # display most commonly used start station
        common_start_stn = df['Start Station'].mode()[0]
        print('Most common start station is:', common_start_stn)

    # display most commonly used end station
        common_end_stn = df['End Station'].mode()[0]
        print('Most common end station is:', common_end_stn)

    # display most frequent combination of start station and end station trip
        df['Mostly_Combined_Stations'] = df['Start Station'] + df['End Station']
        mostly_combined_stns = df['Mostly_Combined_Stations'].mode()[0]
        print('Most frequent combination of start station and end station trip is:', mostly_combined_stns)

    except:
        print('Error occurred, please make sure you provide a correct input option')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # display total travel time
    try:
        print('total travel time', df['Trip Duration'].sum())

    except:
        print('An error occurred, please make sure you provide a correct input option')


    # display mean travel time
    try:
        print('mean travel time', df['Trip Duration'].mean())

    except:
        print('Error occurred, please make sure you provide a correct input option')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)





def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = (df['User Type']).value_counts()
    print('counts of user types \n',user_types)
    print()
    print()

    # Display counts of gender
    print('\nCalculating User Gender Counts...\n')
    try:
        user_gender_count = (df['Gender']).value_counts()
        print('counts of gender\n', user_gender_count)
    except:
        print('Gender data are only available to Chicago and New York States')

    print()
    print()

    # Display earliest, most recent, and most common year of birth
    print('\nCalculating Users earliest, most recent, and most common year of birth...\n')

    try:
        earliest_birthyear = df['Birth Year'].sort_values(ascending=True)
        print('earliest birth year is:', int(earliest_birthyear[0:1].values))
    except (TypeError, ValueError, KeyError):
        print('no data available about the earliest birth year for the given user inputs ')

    print()
    print()

    try:
        most_rec_year =  df['Birth Year'].sort_values(ascending=False)
        print('most recent birth year is:', int(most_rec_year[0:1].values))
    except:
        print('no data available about the most recent birth year for the given user inputs ')

    print()
    print()

    try:
        most_comn_year =  df['Birth Year'].mode()[0]
        print('most common birth year is:', int(most_comn_year))
    except:
        print('no data available about the most common birth year for the given user inputs ')

    print('-'*120)





def data_disp(df):
    ''' Display some raw data to the user '''
    index = 0
    while index <= df.shape[0]:
        query = input('Would you like to see some raw data? Enter yes or no.\n')
        if query.lower() != 'yes':
            break
        else:
            for i in df:
                with pd.option_context('display.max_rows', 5,
                           'display.max_columns', None,
                           'display.width', 100,
                           'display.precision', 3,
                           'display.colheader_justify', 'center'):
                    display(df[:][index: index+5])
                index += 5
                query = input('Would you like to see more raw data? Enter yes or no.\n')
                if query.lower() != 'yes':
                    break
        if query.lower() != 'yes':
                    break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_disp(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
