#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/delete-report-definition.html
	describe-report-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/describe-report-definitions.html
	modify-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/modify-report-definition.html
    """

    write_parameter("cur", "put-report-definition")