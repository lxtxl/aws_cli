#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/check-domain-availability.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain-name : The name of the domain that you want to get availability for. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see Domains that You Can Register with Amazon Route 53 in the Amazon Route 53 Developer Guide .
The domain name can contain only the following characters:

Letters a through z. Domain names are not case sensitive.
Numbers 0 through 9.
Hyphen (-). You canât specify a hyphen at the beginning or end of a label.
Period (.) to separate the labels in the name, such as the . in example.com .

Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see Domains that You Can Register with Amazon Route 53 . For more information, see Formatting Internationalized Domain Names .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53domains", "check-domain-availability", "domain-name", add_option_dict)





