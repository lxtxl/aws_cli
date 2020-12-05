#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-security-configuration.html
if __name__ == '__main__':
    """
	delete-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-security-configuration.html
	describe-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-security-configuration.html
	list-security-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-security-configurations.html
    """

    parameter_display_string = """
    # name : The name of the security configuration.
    # security-configuration : The security configuration details in JSON format. For JSON parameters and examples, see Use Security Configurations to Set Up Cluster Security in the Amazon EMR Management Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "create-security-configuration", "name", "security-configuration", add_option_dict)
