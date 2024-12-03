import re

def is_valid_email(email):
    """
    function thet validate the email
    """
    rexpr = r'[A-z0-9\.]+@[A-z0-9]+\.[A-z]{2,}'
    return re.match(rexpr, email) is not None