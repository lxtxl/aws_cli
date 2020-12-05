#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-network-interface.html
if __name__ == '__main__':
    """
	attach-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-network-interface.html
	create-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-interface.html
	delete-network-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface.html
	describe-network-interfaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html
    """

    parameter_display_string = """
    # attachment-id : The ID of the attachment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "detach-network-interface", "attachment-id", add_option_dict)





