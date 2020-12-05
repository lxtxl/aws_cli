#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-threat-intel-sets.html
if __name__ == '__main__':
    """
	create-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-threat-intel-set.html
	delete-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-threat-intel-set.html
	get-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-threat-intel-set.html
	update-threat-intel-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-threat-intel-set.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that the threatIntelSet is associated with.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("guardduty", "list-threat-intel-sets", "detector-id", add_option_dict)