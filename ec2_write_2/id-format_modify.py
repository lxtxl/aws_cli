#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-id-format.html
if __name__ == '__main__':
    """
	describe-id-format : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-id-format.html
    """

    parameter_display_string = """
    # resource : The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway .
Alternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.
    # use-long-ids | --no-use-long-ids : Indicate whether the resource should use longer IDs (17-character IDs).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "modify-id-format", "resource", "use-long-ids | --no-use-long-ids", add_option_dict)
