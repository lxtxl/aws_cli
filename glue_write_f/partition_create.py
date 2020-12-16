#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition.html
	get-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition.html
	get-partitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partitions.html
	update-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-partition.html
    """

    write_parameter("glue", "create-partition")