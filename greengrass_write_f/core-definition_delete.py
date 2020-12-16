#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-core-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-core-definition.html
	get-core-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-core-definition.html
	list-core-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-core-definitions.html
	update-core-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-core-definition.html
    """

    write_parameter("greengrass", "delete-core-definition")