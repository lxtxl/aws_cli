#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-insight-rules.html
	describe-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-insight-rules.html
	disable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-insight-rules.html
	enable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-insight-rules.html
    """

    write_parameter("cloudwatch", "put-insight-rule")