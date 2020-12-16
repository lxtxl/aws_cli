#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-service-action.html
if __name__ == '__main__':
    """
	delete-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-service-action.html
	describe-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-service-action.html
	list-service-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-service-actions.html
	update-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-service-action.html
    """

    parameter_display_string = """
    # name : The self-service action name.
    # definition-type : The service action definition type. For example, SSM_AUTOMATION .
Possible values:

SSM_AUTOMATION
    # definition : The self-service action definition. Can be one of the following:

Name

The name of the AWS Systems Manager document (SSM document). For example, AWS-RestartEC2Instance .
If you are using a shared SSM document, you must provide the ARN instead of the name.

Version

The AWS Systems Manager automation document version. For example, "Version": "1"

AssumeRole

The Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, "AssumeRole": "arn:aws:iam::12345678910:role/ActionRole" .
To reuse the provisioned product launch role, set to "AssumeRole": "LAUNCH_ROLE" .

Parameters

The list of parameters in JSON format.
For example: [{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}] or [{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}] .

key -> (string)

value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicecatalog", "create-service-action", "name", "definition-type", "definition", add_option_dict)
