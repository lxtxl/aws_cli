#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/update-destination.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream.
    # current-delivery-stream-version-id : Obtain this value from the VersionId result of  DeliveryStreamDescription . This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the VersionId value is updated. The service then performs a merge of the old configuration with the new configuration.
    # destination-id : The ID of the destination.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("firehose", "update-destination", "delivery-stream-name", "current-delivery-stream-version-id", "destination-id", add_option_dict)
