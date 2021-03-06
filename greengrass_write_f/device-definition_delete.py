#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-device-definition.html
	get-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-device-definition.html
	list-device-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-device-definitions.html
	update-device-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-device-definition.html
    """

    write_parameter("greengrass", "delete-device-definition")