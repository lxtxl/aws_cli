#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-stream-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-stream-key.html
	get-stream-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-key.html
	list-stream-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-keys.html
    """

    write_parameter("ivs", "create-stream-key")