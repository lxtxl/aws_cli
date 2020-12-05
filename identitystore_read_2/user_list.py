#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/describe-user.html
if __name__ == '__main__':
    """
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/list-users.html
    """

    parameter_display_string = """
    # identity-store-id : The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string which contains number and lower case letters. This value is generated at the time that a new identity store is created.
    # user-id : The identifier for a user in the identity store.
    """

    execute_two_parameter("identitystore", "describe-user", "identity-store-id", "user-id", parameter_display_string)