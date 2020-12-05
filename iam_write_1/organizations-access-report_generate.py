#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-organizations-access-report.html
if __name__ == '__main__':
    """
	get-organizations-access-report : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-organizations-access-report.html
    """

    parameter_display_string = """
    # entity-path : The path of the AWS Organizations entity (root, OU, or account). You can build an entity path using the known structure of your organization. For example, assume that your account ID is 123456789012 and its parent OU ID is ou-rge0-awsabcde . The organization root ID is r-f6g7h8i9j0example and your organization ID is o-a1b2c3d4e5 . Your entity path is o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-rge0-awsabcde/123456789012 .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "generate-organizations-access-report", "entity-path", add_option_dict)





