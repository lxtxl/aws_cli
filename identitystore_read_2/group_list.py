#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/describe-group.html
if __name__ == '__main__':
    """
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/list-groups.html
    """

    parameter_display_string = """
    # identity-store-id : The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string which contains number and lower case letters. This value is generated at the time that a new identity store is created.
    # group-id : The identifier for a group in the identity store.
    """

    execute_two_parameter("identitystore", "describe-group", "identity-store-id", "group-id", parameter_display_string)