#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-mitigation-action.html
if __name__ == '__main__':
    """
	create-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-mitigation-action.html
	delete-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-mitigation-action.html
	describe-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-mitigation-action.html
	list-mitigation-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigation-actions.html
    """

    parameter_display_string = """
    # action-name : The friendly name for the mitigation action. You canât change the name by using UpdateMitigationAction . Instead, you must delete and re-create the mitigation action with the new name.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "update-mitigation-action", "action-name", add_option_dict)





