#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html
	list-activity-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-activity-types.html
	register-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html
	undeprecate-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-activity-type.html
    """

    write_parameter("swf", "deprecate-activity-type")