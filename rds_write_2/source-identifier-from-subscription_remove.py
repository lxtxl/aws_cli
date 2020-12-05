#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-source-identifier-from-subscription.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # subscription-name : The name of the RDS event notification subscription you want to remove a source identifier from.
    # source-identifier : The source identifier to be removed from the subscription, such as the DB instance identifier for a DB instance or the name of a security group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "remove-source-identifier-from-subscription", "subscription-name", "source-identifier", add_option_dict)
