#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-logger-definition.html
	delete-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-logger-definition.html
	get-logger-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-logger-definition.html
	list-logger-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-logger-definitions.html
    """

    write_parameter("greengrass", "update-logger-definition")