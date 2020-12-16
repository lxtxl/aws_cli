#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-custom-action-type.html
if __name__ == '__main__':
    """
	create-custom-action-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-custom-action-type.html
    """

    parameter_display_string = """
    # category : The category of the custom action that you want to delete, such as source or deploy.
Possible values:

Source
Build
Deploy
Test
Invoke
Approval
    # provider : The provider of the service used in the custom action, such as AWS CodeDeploy.
    # action-version : The version of the custom action to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codepipeline", "delete-custom-action-type", "category", "provider", "action-version", add_option_dict)
