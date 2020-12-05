#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition.html
	delete-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-resource-definition.html
	get-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-resource-definition.html
	list-resource-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-resource-definitions.html
    """

    write_parameter("greengrass", "update-resource-definition")