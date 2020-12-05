#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition.html
	delete-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-function-definition.html
	get-function-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-function-definition.html
	list-function-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-function-definitions.html
    """

    write_parameter("greengrass", "update-function-definition")