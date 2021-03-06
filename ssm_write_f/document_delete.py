#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-document.html
	describe-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html
	get-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html
	list-documents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html
	update-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html
    """

    write_parameter("ssm", "delete-document")