#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone-limit.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # type : The limit that you want to get. Valid values include the following:

MAX_RRSETS_BY_ZONE : The maximum number of records that you can create in the specified hosted zone.
MAX_VPCS_ASSOCIATED_BY_ZONE : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.

Possible values:

MAX_RRSETS_BY_ZONE
MAX_VPCS_ASSOCIATED_BY_ZONE
    # hosted-zone-id : The ID of the hosted zone that you want to get a limit for.
    """

    execute_two_parameter("route53", "get-hosted-zone-limit", "type", "hosted-zone-id", parameter_display_string)