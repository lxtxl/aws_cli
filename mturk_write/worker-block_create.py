#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-worker-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-worker-block.html
	list-worker-blocks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-worker-blocks.html
    """

    write_parameter("mturk", "create-worker-block")