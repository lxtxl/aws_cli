#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-ops-item.html
if __name__ == '__main__':
    """
	describe-ops-items : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-ops-items.html
	get-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html
	update-ops-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-ops-item.html
    """

    parameter_display_string = """
    # description : Information about the OpsItem.
    # source : The origin of the OpsItem, such as Amazon EC2 or Systems Manager.

Note
The source name canât contain the following strings: aws, amazon, and amzn.
    # title : A short heading that describes the nature of the OpsItem and the impacted resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ssm", "create-ops-item", "description", "source", "title", add_option_dict)
