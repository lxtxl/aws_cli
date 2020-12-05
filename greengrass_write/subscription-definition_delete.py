#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-subscription-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-subscription-definition.html
	get-subscription-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-subscription-definition.html
	list-subscription-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-subscription-definitions.html
	update-subscription-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-subscription-definition.html
    """

    write_parameter("greengrass", "delete-subscription-definition")