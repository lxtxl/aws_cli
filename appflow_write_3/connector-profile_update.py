#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-connector-profile.html
if __name__ == '__main__':
    """
	create-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html
	delete-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/delete-connector-profile.html
	describe-connector-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html
    """

    parameter_display_string = """
    # connector-profile-name : The name of the connector profile and is unique for each ConnectorProfile in the AWS Account.
    # connection-mode : Indicates the connection mode and if it is public or private.
Possible values:

Public
Private
    # connector-profile-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appflow", "update-connector-profile", "connector-profile-name", "connection-mode", "connector-profile-config", add_option_dict)
