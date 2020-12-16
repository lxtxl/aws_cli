#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-app.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/create-app.html
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/delete-app.html
	launch-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/launch-app.html
	list-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/list-apps.html
	terminate-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/terminate-app.html
	update-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/update-app.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("sms", "get-app", add_option_dict)