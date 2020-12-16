#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-partition-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition-index.html
	get-partition-indexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition-indexes.html
    """

    write_parameter("glue", "create-partition-index")