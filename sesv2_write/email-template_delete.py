#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-template.html
	get-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-template.html
	list-email-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-email-templates.html
	update-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-email-template.html
    """

    write_parameter("sesv2", "delete-email-template")