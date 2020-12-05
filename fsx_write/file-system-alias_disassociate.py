#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/associate-file-system-aliases.html
	describe-file-system-aliases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-system-aliases.html
    """

    write_parameter("fsx", "disassociate-file-system-aliases")