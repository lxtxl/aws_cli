#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/delete-connector-profile.html
if __name__ == '__main__':
    """
	create-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html
	describe-connector-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html
	update-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-connector-profile.html
    """

    parameter_display_string = """
    # connector-profile-name : The name of the connector profile. The name is unique for each ConnectorProfile in your account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appflow", "delete-connector-profile", "connector-profile-name", add_option_dict)





