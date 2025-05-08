from datetime import datetime, timedelta
import os
import json

def calculate_due_date(start_date, weeks = 2):
    """Calculate due date (2 weeks from loan date)"""
    return start_date + datetime.timedelta(weeks=weeks)

def format_date_for_display(date_obj):
    """Format date for user-friendly display like '08 Mayıs 2025, 14:30'."""
    return date_obj.strftime('%Y-%m-%d')

def is_date_overdue(due_date):
    """Check if a due date has passed"""
    return due_date < datetime.now()

def parse_date_string(date_str):
    """Parse a date string like '2025-05-08-14:30:00' into a datetime object."""
    return datetime.strptime(date_str, '%Y-%m-%d-%H:%M:%S')
