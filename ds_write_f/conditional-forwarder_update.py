#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-conditional-forwarder.html
	delete-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-conditional-forwarder.html
	describe-conditional-forwarders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-conditional-forwarders.html
    """

    write_parameter("ds", "update-conditional-forwarder")