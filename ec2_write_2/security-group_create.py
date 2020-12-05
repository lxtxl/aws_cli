#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-security-group.html
if __name__ == '__main__':
    """
	delete-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-security-group.html
	describe-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html
    """

    parameter_display_string = """
    # description : A description for the security group. This is informational only.
Constraints: Up to 255 characters in length
Constraints for EC2-Classic: ASCII characters
Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
    # group-name : The name of the security group.
Constraints: Up to 255 characters in length. Cannot start with sg- .
Constraints for EC2-Classic: ASCII characters
Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-security-group", "description", "group-name", add_option_dict)
