import datetime
from datetime import timedelta

current_date = datetime.datetime.now(datetime.UTC)
print(current_date)


class AuditRecord:
    def __init__(self, action: str):
        self.action = action
        self.created_at = datetime.datetime.now(datetime.UTC)


record = AuditRecord("create")
print(record.created_at)



date_as_text = "25 November, 2025 10:30"
# manual_date = datetime.datetime(2025, 11, 25)

parsed_datetime = datetime.datetime.strptime(date_as_text, "%d %B, %Y %H:%M")
print(parsed_datetime)

date_as_text = parsed_datetime.strftime("%d %B %Y")
print(date_as_text)


# filters
utc_now = datetime.datetime.now(datetime.UTC)
print(f"before: {utc_now}")

week_ago = utc_now - timedelta(days=7)
print(f"after: {week_ago}")

# where user.created_at > week_ago

print(week_ago > utc_now)
print(week_ago < utc_now)

print(utc_now.day)
print(utc_now.date())