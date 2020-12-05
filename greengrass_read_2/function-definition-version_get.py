#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition-version.html
if __name__ == '__main__':
    """
	create-function-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition-version.html
	list-function-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definition-versions.html
    """

    parameter_display_string = """
    # function-definition-id : The ID of the Lambda function definition.
    # function-definition-version-id : The ID of the function definition version. This value maps to the ââVersionââ property of the corresponding ââVersionInformationââ object, which is returned by ââListFunctionDefinitionVersionsââ requests. If the version is the last one that was associated with a function definition, the value also maps to the ââLatestVersionââ property of the corresponding ââDefinitionInformationââ object.
    """

    execute_two_parameter("greengrass", "get-function-definition-version", "function-definition-id", "function-definition-version-id", parameter_display_string)