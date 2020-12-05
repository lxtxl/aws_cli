#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html
	list-workflow-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html
	register-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html
	undeprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html
    """

    write_parameter("swf", "deprecate-workflow-type")