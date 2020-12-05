#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-ml-transform.html
	get-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transform.html
	get-ml-transforms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transforms.html
	list-ml-transforms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-ml-transforms.html
	update-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-ml-transform.html
    """

    write_parameter("glue", "delete-ml-transform")