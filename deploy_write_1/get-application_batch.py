#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-applications.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-names : A list of application names separated by spaces. The maximum number of application names you can specify is 100.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("deploy", "batch-get-applications", "application-names", add_option_dict)





