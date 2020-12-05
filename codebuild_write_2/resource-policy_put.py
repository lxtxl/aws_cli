#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/put-resource-policy.html
if __name__ == '__main__':
    """
	delete-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-resource-policy.html
	get-resource-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/get-resource-policy.html
    """

    parameter_display_string = """
    # policy : A JSON-formatted resource policy. For more information, see Sharing a Project and Sharing a Report Group in the AWS CodeBuild User Guide .
    # resource-arn : The ARN of the Project or ReportGroup resource you want to associate with a resource policy.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codebuild", "put-resource-policy", "policy", "resource-arn", add_option_dict)
