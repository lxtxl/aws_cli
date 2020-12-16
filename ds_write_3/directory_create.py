#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-directory.html
if __name__ == '__main__':
    """
	connect-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/connect-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-directory.html
	describe-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html
	share-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/share-directory.html
	unshare-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/unshare-directory.html
    """

    parameter_display_string = """
    # name : The fully qualified name for the directory, such as corp.example.com .
    # password : The password for the directory administrator. The directory creation process creates a directory administrator account with the user name Administrator and this password.
If you need to change the password for the administrator account, you can use the  ResetUserPassword API call.
The regex pattern for this string is made up of the following conditions:

Length (?=^.{8,64}$) â Must be between 8 and 64 characters

AND any 3 of the following password complexity rules required by Active Directory:

Numbers and upper case and lowercase (?=.*d)(?=.*[A-Z])(?=.*[a-z])
Numbers and special characters and lower case (?=.*d)(?=.*[^A-Za-z0-9s])(?=.*[a-z])
Special characters and upper case and lower case (?=.*[^A-Za-z0-9s])(?=.*[A-Z])(?=.*[a-z])
Numbers and upper case and special characters (?=.*d)(?=.*[A-Z])(?=.*[^A-Za-z0-9s])

For additional information about how Active Directory passwords are enforced, see Password must meet complexity requirements on the Microsoft website.
    # size : The size of the directory.
Possible values:

Small
Large
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "create-directory", "name", "password", "size", add_option_dict)
