#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html
if __name__ == '__main__':
    """
	deprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-workflow-type.html
	list-workflow-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html
	register-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html
	undeprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html
    """

    parameter_display_string = """
    # domain : The name of the domain in which this workflow type is registered.
    # workflow-type : 
    """

    execute_two_parameter("swf", "describe-workflow-type", "domain", "workflow-type", parameter_display_string)