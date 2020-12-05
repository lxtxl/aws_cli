#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/detach-volume.html
if __name__ == '__main__':
    """
	attach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/attach-volume.html
	delete-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-volume.html
	list-volumes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volumes.html
    """

    parameter_display_string = """
    # volume-arn : The Amazon Resource Name (ARN) of the volume to detach from the gateway.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "detach-volume", "volume-arn", add_option_dict)





