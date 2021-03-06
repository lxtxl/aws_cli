#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-suppressed-destination.html
	get-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-suppressed-destination.html
	list-suppressed-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-suppressed-destinations.html
    """

    write_parameter("sesv2", "put-suppressed-destination")