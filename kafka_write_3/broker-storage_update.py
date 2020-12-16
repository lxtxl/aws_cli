#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-broker-storage.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-arn : The Amazon Resource Name (ARN) that uniquely identifies the cluster.
    # current-version : The version of cluster to update from. A successful operation will then generate a new version.
    # target-broker-ebs-volume-info : Describes the target volume size and the ID of the broker to apply the update to.

(structure)

Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.
KafkaBrokerNodeId -> (string)

The ID of the broker to update.

VolumeSizeGB -> (integer)

Size of the EBS volume to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kafka", "update-broker-storage", "cluster-arn", "current-version", "target-broker-ebs-volume-info", add_option_dict)
