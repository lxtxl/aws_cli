#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/test-dns-answer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # hosted-zone-id : The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
    # record-name : The name of the resource record set that you want Amazon Route 53 to simulate a query for.
    # record-type : The type of the resource record set.
Possible values:

SOA
A
TXT
NS
CNAME
MX
NAPTR
PTR
SRV
SPF
AAAA
CAA
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("route53", "test-dns-answer", "hosted-zone-id", "record-name", "record-type", add_option_dict)
