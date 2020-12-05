#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-resource.html
	get-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resource.html
	get-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/tag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-resource.html
    """

    write_parameter("apigateway", "untag-resource")