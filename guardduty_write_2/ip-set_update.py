#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-ip-set.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-ip-set.html
	delete-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-ip-set.html
	get-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-ip-sets.html
    """

    parameter_display_string = """
    # detector-id : The detectorID that specifies the GuardDuty service whose IPSet you want to update.
    # ip-set-id : The unique ID that specifies the IPSet that you want to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "update-ip-set", "detector-id", "ip-set-id", add_option_dict)
