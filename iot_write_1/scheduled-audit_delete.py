#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-scheduled-audit.html
if __name__ == '__main__':
    """
	create-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-scheduled-audit.html
	describe-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-scheduled-audit.html
	list-scheduled-audits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-scheduled-audits.html
	update-scheduled-audit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-scheduled-audit.html
    """

    parameter_display_string = """
    # scheduled-audit-name : The name of the scheduled audit you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-scheduled-audit", "scheduled-audit-name", add_option_dict)





