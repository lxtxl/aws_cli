#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-image.html
if __name__ == '__main__':
    """
	copy-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html
	deregister-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html
	describe-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html
	export-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-image.html
	import-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html
	register-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html
    """

    parameter_display_string = """
    # instance-id : The ID of the instance.
    # name : A name for the new image.
Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes (â), at-signs (@), or underscores(_)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-image", "instance-id", "name", add_option_dict)
