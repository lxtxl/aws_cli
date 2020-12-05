#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition.html
	delete-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-connector-definition.html
	get-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition.html
	list-connector-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definitions.html
    """

    write_parameter("greengrass", "update-connector-definition")