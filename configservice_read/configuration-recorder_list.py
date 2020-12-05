#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html
if __name__ == '__main__':
    """
	delete-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-configuration-recorder.html
	put-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-recorder.html
	start-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-configuration-recorder.html
	stop-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/stop-configuration-recorder.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("configservice", "describe-configuration-recorders", add_option_dict)