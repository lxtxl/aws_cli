#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-registry.html
	describe-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-registry.html
	list-registries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-registries.html
	update-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-registry.html
    """

    write_parameter("schemas", "create-registry")