#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition-version.html
if __name__ == '__main__':
    """
	create-device-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition-version.html
	list-device-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definition-versions.html
    """

    parameter_display_string = """
    # device-definition-id : The ID of the device definition.
    # device-definition-version-id : The ID of the device definition version. This value maps to the ââVersionââ property of the corresponding ââVersionInformationââ object, which is returned by ââListDeviceDefinitionVersionsââ requests. If the version is the last one that was associated with a device definition, the value also maps to the ââLatestVersionââ property of the corresponding ââDefinitionInformationââ object.
    """

    execute_two_parameter("greengrass", "get-device-definition-version", "device-definition-id", "device-definition-version-id", parameter_display_string)