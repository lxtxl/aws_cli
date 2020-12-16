#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-fleets.html
if __name__ == '__main__':
    """
	associate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/associate-fleet.html
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-fleet.html
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-fleet.html
	disassociate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/disassociate-fleet.html
	start-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-fleet.html
	stop-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-fleet.html
	update-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-fleet.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("appstream", "describe-fleets", add_option_dict)