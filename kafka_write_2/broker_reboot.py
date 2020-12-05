#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/reboot-broker.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # broker-ids : The list of broker IDs to be rebooted. The reboot-broker operation supports rebooting one broker at a time.

(string)
    # cluster-arn : The Amazon Resource Name (ARN) of the cluster to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kafka", "reboot-broker", "broker-ids", "cluster-arn", add_option_dict)
