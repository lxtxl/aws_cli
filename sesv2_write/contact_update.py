#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact.html
	delete-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact.html
	get-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact.html
	list-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contacts.html
    """

    write_parameter("sesv2", "update-contact")