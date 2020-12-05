#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-directory.html
	disable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/disable-directory.html
	get-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-directory.html
	list-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-directories.html
    """

    write_parameter("clouddirectory", "enable-directory")