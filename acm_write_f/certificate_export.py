#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html
	renew-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html
	request-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html
    """

    write_parameter("acm", "export-certificate")