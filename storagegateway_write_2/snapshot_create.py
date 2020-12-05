#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # volume-arn : The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a list of gateway volumes.
    # snapshot-description : Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the Description field, and in the AWS Storage Gateway snapshot Details pane, Description field.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "create-snapshot", "volume-arn", "snapshot-description", add_option_dict)
