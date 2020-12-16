#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-registry.html
	get-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-registry.html
	list-registries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-registries.html
	update-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-registry.html
    """

    write_parameter("glue", "delete-registry")