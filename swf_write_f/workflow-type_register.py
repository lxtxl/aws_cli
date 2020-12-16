#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-workflow-type.html
	describe-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html
	list-workflow-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html
	undeprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html
    """

    write_parameter("swf", "register-workflow-type")