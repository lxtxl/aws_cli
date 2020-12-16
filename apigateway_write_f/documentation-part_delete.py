#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-documentation-part.html
	get-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-part.html
	get-documentation-parts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-documentation-parts.html
	import-documentation-parts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-documentation-parts.html
	update-documentation-part : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-documentation-part.html
    """

    write_parameter("apigateway", "delete-documentation-part")