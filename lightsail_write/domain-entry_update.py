#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-domain-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-domain-entry.html
	delete-domain-entry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-domain-entry.html
    """

    write_parameter("lightsail", "update-domain-entry")