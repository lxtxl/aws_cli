#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-ip-set.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-ip-set.html
	delete-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-ip-set.html
	get-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-ip-sets.html
    """

    parameter_display_string = """
    # ip-set-id : The IPSetId of the  IPSet that you want to update. IPSetId is returned by  CreateIPSet and by  ListIPSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    # updates : An array of IPSetUpdate objects that you want to insert into or delete from an  IPSet . For more information, see the applicable data types:

IPSetUpdate : Contains Action and IPSetDescriptor
IPSetDescriptor : Contains Type and Value

You can insert a maximum of 1000 addresses in a single request.
(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the type of update to perform to an  IPSet with  UpdateIPSet .
Action -> (string)

Specifies whether to insert or delete an IP address with  UpdateIPSet .

IPSetDescriptor -> (structure)

The IP address type (IPV4 or IPV6 ) and the IP address range (in CIDR notation) that web requests originate from.
Type -> (string)

Specify IPV4 or IPV6 .

Value -> (string)

Specify an IPv4 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify 192.0.2.44/32 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify 192.0.2.0/24 .

For more information about CIDR notation, see the Wikipedia entry Classless Inter-Domain Routing .
Specify an IPv6 address by using CIDR notation. For example:

To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify 1111:0000:0000:0000:0000:0000:0000:0111/128 .
To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify 1111:0000:0000:0000:0000:0000:0000:0000/64 .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "update-ip-set", "ip-set-id", "change-token", "updates", add_option_dict)
