#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-custom-verification-email-template.html
	get-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-custom-verification-email-template.html
	list-custom-verification-email-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-custom-verification-email-templates.html
	update-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-custom-verification-email-template.html
    """

    write_parameter("sesv2", "delete-custom-verification-email-template")