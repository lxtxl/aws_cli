#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html
	delete-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-key-pair.html
	describe-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-key-pairs.html
    """

    write_parameter("ec2", "import-key-pair")