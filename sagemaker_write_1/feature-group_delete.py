#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-feature-group.html
if __name__ == '__main__':
    """
	create-feature-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-feature-group.html
	describe-feature-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-feature-group.html
	list-feature-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-feature-groups.html
    """

    parameter_display_string = """
    # feature-group-name : The name of the FeatureGroup you want to delete. The name must be unique within an AWS Region in an AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-feature-group", "feature-group-name", add_option_dict)





