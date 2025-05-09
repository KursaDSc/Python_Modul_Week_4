from datetime import datetime, timedelta

def calculate_due_date(start_date, weeks = 2):
    """Calculate due date (2 weeks from loan date)"""
    return start_date + timedelta(weeks=weeks)

def is_date_overdue(due_date):
    """Check if a due date has passed"""
    return due_date < datetime.now()

def parse_date_string(date_str):
    """Parse a date string like '2025-05-08' into a datetime object."""
    return datetime.strptime(date_str, '%Y-%m-%d')

def to_date_string(date_obj):
    """Convert datetime object to string like '2025-05-08' for saving"""
    return date_obj.strftime('%Y-%m-%d')
