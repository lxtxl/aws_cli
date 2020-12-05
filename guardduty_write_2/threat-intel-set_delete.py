#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-threat-intel-set.html
if __name__ == '__main__':
    """
	create-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-threat-intel-set.html
	get-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-threat-intel-set.html
	list-threat-intel-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-threat-intel-sets.html
	update-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-threat-intel-set.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that the threatIntelSet is associated with.
    # threat-intel-set-id : The unique ID of the threatIntelSet that you want to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "delete-threat-intel-set", "detector-id", "threat-intel-set-id", add_option_dict)
