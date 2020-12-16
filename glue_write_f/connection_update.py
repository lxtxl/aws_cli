#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-connection.html
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-connection.html
	get-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connection.html
	get-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connections.html
    """

    write_parameter("glue", "update-connection")