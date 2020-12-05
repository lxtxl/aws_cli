#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/rotate-ingest-endpoint-credentials.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # id : The ID of the channel the IngestEndpoint is on.
    # ingest-endpoint-id : The id of the IngestEndpoint whose credentials should be rotated
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediapackage", "rotate-ingest-endpoint-credentials", "id", "ingest-endpoint-id", add_option_dict)
