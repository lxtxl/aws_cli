#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/resend-validation-email.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # certificate-arn : String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the  RequestCertificate action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form:

arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
    # domain : The fully qualified domain name (FQDN) of the certificate that needs to be validated.
    # validation-domain : The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the Domain value or a superdomain of the Domain value. For example, if you requested a certificate for site.subdomain.example.com and specify a ValidationDomain of subdomain.example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:

admin@subdomain.example.com
administrator@subdomain.example.com
hostmaster@subdomain.example.com
postmaster@subdomain.example.com
webmaster@subdomain.example.com
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("acm", "resend-validation-email", "certificate-arn", "domain", "validation-domain", add_option_dict)
