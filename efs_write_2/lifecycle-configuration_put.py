#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/put-lifecycle-configuration.html
if __name__ == '__main__':
    """
	describe-lifecycle-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-lifecycle-configuration.html
    """

    parameter_display_string = """
    # file-system-id : The ID of the file system for which you are creating the LifecycleConfiguration object (String).
    # lifecycle-policies : An array of LifecyclePolicy objects that define the file systemâs LifecycleConfiguration object. A LifecycleConfiguration object tells lifecycle management when to transition files from the Standard storage class to the Infrequent Access storage class.
(structure)

Describes a policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.
TransitionToIA -> (string)

A value that describes the period of time that a file is not accessed, after which it transitions to the IA storage class. Metadata operations such as listing the contents of a directory donât count as file access events.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "put-lifecycle-configuration", "file-system-id", "lifecycle-policies", add_option_dict)
