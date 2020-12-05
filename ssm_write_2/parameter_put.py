#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html
if __name__ == '__main__':
    """
	delete-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html
	delete-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameters.html
	describe-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html
	get-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html
	get-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html
    """

    parameter_display_string = """
    # name : The fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy, you must include a leading forward slash character (/) when you create or reference a parameter. For example: /Dev/DBServer/MySQL/db-string13
Naming Constraints:

Parameter names are case sensitive.
A parameter name must be unique within an AWS Region
A parameter name canât be prefixed with âawsâ or âssmâ (case-insensitive).
Parameter names can include only the following symbols and letters: a-zA-Z0-9_.-/
A parameter name canât include spaces.
Parameter hierarchies are limited to a maximum depth of fifteen levels.

For additional information about valid values for parameter names, see About requirements and constraints for parameter names in the AWS Systems Manager User Guide .

Note
The maximum length constraint listed below includes capacity for additional system attributes that are not part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters:

arn:aws:ssm:us-east-2:111122223333:parameter/ExampleParameterName
    # value : The parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB.

Note
Parameters canât be referenced or nested in the values of other parameters. You canât include {{}} or {{ssm:*parameter-name* }} in a parameter value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "put-parameter", "name", "value", add_option_dict)
