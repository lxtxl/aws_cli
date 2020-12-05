#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-configuration-recorder.html
if __name__ == '__main__':
    """
	describe-configuration-recorders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html
	put-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-recorder.html
	start-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-configuration-recorder.html
	stop-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/stop-configuration-recorder.html
    """

    parameter_display_string = """
    # configuration-recorder-name : The name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the DescribeConfigurationRecorders action.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "delete-configuration-recorder", "configuration-recorder-name", add_option_dict)





