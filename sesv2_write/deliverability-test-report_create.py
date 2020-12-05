#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-deliverability-test-report : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-deliverability-test-report.html
	list-deliverability-test-reports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-deliverability-test-reports.html
    """

    write_parameter("sesv2", "create-deliverability-test-report")