def get_email_from_input():
    """Contains '@' and '.' """
    email = input("Write down your email: ")
    if "@" not in email or "." not in email:
        print('Email is not valid.')
    else:
        return email


def get_user_name_from_input():
    """ Not empty string. No spaces. """
    try:
        username = input("Write down your user name: ")
        if len(username) == 0 or " " in username:
            print('username is not valid.')
        else:
            return username
    except:
        pass


def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special
    character and one letter"""
    return input("Create your password: ")
