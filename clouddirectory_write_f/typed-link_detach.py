#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-typed-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-typed-link.html
    """

    write_parameter("clouddirectory", "detach-typed-link")