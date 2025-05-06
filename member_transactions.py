import book_transactions
import os
import json

def add_member(name, phone, address):
    """Register a new library member"""
    pass

def delete_member(member_id):
    """Remove a member from the system"""
    pass

def search_member(search_term):
    """Search members by various criteria"""
    pass

def get_all_members():
    """Retrieve list of all members"""
    pass

def show_members():
    """Show list of all members"""
    pass

def update_member(member_id, field, new_value):
    """Update member information"""
    pass

def member_exists(member_id):
    """Check if a member exists in the system"""
    pass


def save_tracking():
    """save updates to tracking.json file"""

def get_tracking():
    """load tracking data from tracking.json file"""

def lend_book(member_id, book_barcode, loan_date, return_date):
    """Process book loan to a member"""
    pass

def return_book(member_id, book_barcode):
    """Process book return from a member"""
    pass

def get_loan_history(member_id=None):
    """Retrieve loan history (all or for specific member)"""
    pass

def get_overdue_loans():
    """Identify books that are overdue"""
    pass

def update_loan_status(loan_id, status):
    """Update the status of a loan"""
    pass