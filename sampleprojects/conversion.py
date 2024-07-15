def convert_days(days):
     years_in_days = 365
     weeks_in_days = 7
     years = days // years_in_days
     remaining_days = days % years_in_days
     weeks = remaining_days // weeks_in_days
     remaining_days = remaining_days % weeks_in_days
     return years, weeks, remaining_days
days = int(input("Enter the number of days: "))
years, weeks, remaining_days = convert_days(days)
print(f"{days} days is equivalent to:")
print(f"{years} years")
print(f"{weeks} weeks")
print(f"{remaining_days} days")