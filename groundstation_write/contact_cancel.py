#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/describe-contact.html
	list-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-contacts.html
	reserve-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/reserve-contact.html
    """

    write_parameter("groundstation", "cancel-contact")