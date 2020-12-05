#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-usage-limit.html
if __name__ == '__main__':
    """
	create-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-usage-limit.html
	delete-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-usage-limit.html
	describe-usage-limits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-usage-limits.html
    """

    parameter_display_string = """
    # usage-limit-id : The identifier of the usage limit to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "modify-usage-limit", "usage-limit-id", add_option_dict)





