#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html
	list-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html
	unarchive-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/unarchive-findings.html
    """

    write_parameter("guardduty", "archive-findings")