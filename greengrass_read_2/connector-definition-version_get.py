#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition-version.html
if __name__ == '__main__':
    """
	create-connector-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition-version.html
	list-connector-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definition-versions.html
    """

    parameter_display_string = """
    # connector-definition-id : The ID of the connector definition.
    # connector-definition-version-id : The ID of the connector definition version. This value maps to the ââVersionââ property of the corresponding ââVersionInformationââ object, which is returned by ââListConnectorDefinitionVersionsââ requests. If the version is the last one that was associated with a connector definition, the value also maps to the ââLatestVersionââ property of the corresponding ââDefinitionInformationââ object.
    """

    execute_two_parameter("greengrass", "get-connector-definition-version", "connector-definition-id", "connector-definition-version-id", parameter_display_string)