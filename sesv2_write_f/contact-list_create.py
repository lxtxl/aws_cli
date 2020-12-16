#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact-list.html
	get-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact-list.html
	list-contact-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contact-lists.html
	update-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact-list.html
    """

    write_parameter("sesv2", "create-contact-list")