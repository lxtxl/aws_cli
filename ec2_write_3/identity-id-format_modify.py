#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-identity-id-format.html
if __name__ == '__main__':
    """
	describe-identity-id-format : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-identity-id-format.html
    """

    parameter_display_string = """
    # principal-arn : The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for all IAM users, IAM roles, and the root user of the account.
    # resource : The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway .
Alternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.
    # use-long-ids | --no-use-long-ids : Indicates whether the resource should use longer IDs (17-character IDs)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "modify-identity-id-format", "principal-arn", "resource", "use-long-ids | --no-use-long-ids", add_option_dict)
