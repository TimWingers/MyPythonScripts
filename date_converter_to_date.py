from datetime import datetime as dt
def convert2date (strdate):
    if strdate == themoscowtimes:
        res = dt.strptime(strdate, '%A, %B %d, %Y')
    elif strdate == theguardian:
        res = dt.strptime(strdate, '%A, %d.%m.%y')
    elif strdate == dailynews:
        res = dt.strptime(strdate, '%A, %d %B %Y')
    return res

themoscowtimes = 'Wednesday, October 2, 2002' 
theguardian = 'Friday, 11.10.13'
dailynews = 'Thursday, 18 August 1977'
convert2date(themoscowtimes)
#datetime.datetime(2002, 10, 2, 0, 0)
convert2date(theguardian)
#datetime.datetime(2013, 10, 11, 0, 0)
convert2date(dailynews)
#datetime.datetime(1977, 8, 18, 0, 0)