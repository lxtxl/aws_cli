#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-contact-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-contact-method.html
	get-contact-methods : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-contact-methods.html
    """

    write_parameter("lightsail", "delete-contact-method")