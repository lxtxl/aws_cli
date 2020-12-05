#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-dev-endpoint.html
	get-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoint.html
	get-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-dev-endpoints.html
	list-dev-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-dev-endpoints.html
	update-dev-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-dev-endpoint.html
    """

    write_parameter("glue", "create-dev-endpoint")