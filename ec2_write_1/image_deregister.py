#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html
if __name__ == '__main__':
    """
	copy-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-image.html
	describe-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html
	export-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-image.html
	import-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html
	register-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html
    """

    parameter_display_string = """
    # image-id : The ID of the AMI.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "deregister-image", "image-id", add_option_dict)




