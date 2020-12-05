#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	add-flow-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-sources.html
	update-flow-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-source.html
    """

    write_parameter("mediaconnect", "remove-flow-source")