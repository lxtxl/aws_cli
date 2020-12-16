#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-service-integration.html
if __name__ == '__main__':
    """
	describe-service-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-service-integration.html
    """

    parameter_display_string = """
    # service-integration : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devops-guru", "update-service-integration", "service-integration", add_option_dict)





