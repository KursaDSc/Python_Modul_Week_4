from datetime import datetime, timedelta
import os
import json


def get_current_datetime():
    """Get current date and time in standard format ('YYYY-MM-DDTHH:MM:SS')"""
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def calculate_due_date(start_date, weeks = 2):
    """Calculate due date (2 weeks from loan date)"""
    return start_date + datetime.timedelta(weeks=weeks)

def format_date_for_display(date_obj):
    """Format date for user-friendly display"""
    pass

def is_date_overdue(due_date):
    """Check if a due date has passed"""
    pass

def parse_date_string(date_str):
    """Convert date string to date object"""
    pass
