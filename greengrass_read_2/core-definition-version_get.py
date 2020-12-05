#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-core-definition-version.html
if __name__ == '__main__':
    """
	create-core-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-core-definition-version.html
	list-core-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-core-definition-versions.html
    """

    parameter_display_string = """
    # core-definition-id : The ID of the core definition.
    # core-definition-version-id : The ID of the core definition version. This value maps to the ââVersionââ property of the corresponding ââVersionInformationââ object, which is returned by ââListCoreDefinitionVersionsââ requests. If the version is the last one that was associated with a core definition, the value also maps to the ââLatestVersionââ property of the corresponding ââDefinitionInformationââ object.
    """

    execute_two_parameter("greengrass", "get-core-definition-version", "core-definition-id", "core-definition-version-id", parameter_display_string)