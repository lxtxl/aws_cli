#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource.html
if __name__ == '__main__':
    """
	describe-stack-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resources.html
	list-stack-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-resources.html
    """

    parameter_display_string = """
    # stack-name : The name or the unique stack ID that is associated with the stack, which are not always interchangeable:

Running stacks: You can specify either the stackâs name or its unique stack ID.
Deleted stacks: You must specify the unique stack ID.

Default: There is no default value.
    # logical-resource-id : The logical name of the resource as specified in the template.
Default: There is no default value.
    """

    execute_two_parameter("cloudformation", "describe-stack-resource", "stack-name", "logical-resource-id", parameter_display_string)