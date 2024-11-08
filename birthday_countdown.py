from datetime import datetime, timedelta
birth_month = int(input())
today = datetime.today()

if birth_month >= today.month:
    birthday_month = datetime(today.year, birth_month, today.day)
else:
    birthday_month = datetime(today.year + 1, birth_month, today.day)

time_until_birthday = birthday_month - today
months_until_birthday = (birthday_month.year - today.year) * 12 + (birthday_month.month - today.month)
days_until_birthday = time_until_birthday.days % 30

print(f"You have {months_until_birthday} months and {days_until_birthday} days until it's your birthday month!")