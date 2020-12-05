#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/update-security-group-rule-descriptions-egress.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # ip-permissions : The IP permissions for the security group rule.
(structure)

Describes a set of permissions for a security group rule.
FromPort -> (integer)

The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.

IpProtocol -> (string)

The IP protocol name (tcp , udp , icmp , icmpv6 ) or number (see Protocol Numbers ).
[VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or icmpv6 allows traffic on all ports, regardless of any port range you specify. For tcp , udp , and icmp , you must specify a port range. For icmpv6 , the port range is optional; if you omit the port range, traffic for all types and codes is allowed.

IpRanges -> (list)

The IPv4 ranges.
(structure)

Describes an IPv4 range.
CidrIp -> (string)

The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.

Description -> (string)

A description for the security group rule that references this IPv4 address range.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*



Ipv6Ranges -> (list)

[VPC only] The IPv6 ranges.
(structure)

[EC2-VPC only] Describes an IPv6 range.
CidrIpv6 -> (string)

The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.

Description -> (string)

A description for the security group rule that references this IPv6 address range.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*



PrefixListIds -> (list)

[VPC only] The prefix list IDs.
(structure)

Describes a prefix list ID.
Description -> (string)

A description for the security group rule that references this prefix list ID.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

PrefixListId -> (string)

The ID of the prefix.



ToPort -> (integer)

The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.

UserIdGroupPairs -> (list)

The security group and AWS account ID pairs.
(structure)

Describes a security group and AWS account ID pair.
Description -> (string)

A description for the security group rule that references this user ID group pair.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.

PeeringStatus -> (string)

The status of a VPC peering connection, if applicable.

UserId -> (string)

The ID of an AWS account.
For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.

VpcId -> (string)

The ID of the VPC for the referenced security group, if applicable.

VpcPeeringConnectionId -> (string)

The ID of the VPC peering connection, if applicable.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "update-security-group-rule-descriptions-egress", "ip-permissions", add_option_dict)





