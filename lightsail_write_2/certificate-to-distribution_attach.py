#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-certificate-to-distribution.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # distribution-name : The name of the distribution that the certificate will be attached to.
Use the GetDistributions action to get a list of distribution names that you can specify.
    # certificate-name : The name of the certificate to attach to a distribution.
Only certificates with a status of ISSUED can be attached to a distribution.
Use the GetCertificates action to get a list of certificate names that you can specify.

Note
This is the name of the certificate resource type and is used only to reference the certificate in other API actions. It can be different than the domain name of the certificate. For example, your certificate name might be WordPress-Blog-Certificate and the domain name of the certificate might be example.com .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "attach-certificate-to-distribution", "distribution-name", "certificate-name", add_option_dict)
