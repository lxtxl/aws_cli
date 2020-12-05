#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group-version.html
if __name__ == '__main__':
    """
	create-group-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-group-version.html
	list-group-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-group-versions.html
    """

    parameter_display_string = """
    # group-id : The ID of the Greengrass group.
    # group-version-id : The ID of the group version. This value maps to the ââVersionââ property of the corresponding ââVersionInformationââ object, which is returned by ââListGroupVersionsââ requests. If the version is the last one that was associated with a group, the value also maps to the ââLatestVersionââ property of the corresponding ââGroupInformationââ object.
    """

    execute_two_parameter("greengrass", "get-group-version", "group-id", "group-version-id", parameter_display_string)