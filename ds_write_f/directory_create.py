#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	connect-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/connect-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-directory.html
	describe-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html
	share-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/share-directory.html
	unshare-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/unshare-directory.html
    """

    write_parameter("ds", "create-directory")