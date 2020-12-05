#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-shared-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-shared-directories.html
	reject-shared-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/reject-shared-directory.html
    """

    write_parameter("ds", "accept-shared-directory")