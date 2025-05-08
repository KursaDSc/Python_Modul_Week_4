import os
import json
import core.time_utils as tu
import data_io

def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", "r", encoding= 'udf-8') as f:
            return json.load(f)
    except:
        return []
def save_members(member):
    with open("members.json", 'w', encoding= 'udf-8') as f:
        json.dump(member, f, indent=4, ensure_ascii=False)

def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
    
def save_members(members):
    with open("members.json", 'w', encoding='utf-8') as f:
        json.dump(members, f, indent=4, ensure_ascii=False)      

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
