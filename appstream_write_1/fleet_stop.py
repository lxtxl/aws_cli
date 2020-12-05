#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-fleet.html
if __name__ == '__main__':
    """
	associate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/associate-fleet.html
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-fleet.html
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-fleet.html
	describe-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-fleets.html
	disassociate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/disassociate-fleet.html
	start-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-fleet.html
	update-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-fleet.html
    """

    parameter_display_string = """
    # name : The name of the fleet.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "stop-fleet", "name", add_option_dict)





