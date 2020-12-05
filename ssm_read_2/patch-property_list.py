#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-properties.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # operating-system : The operating system type for which to list patches.
Possible values:

WINDOWS
AMAZON_LINUX
AMAZON_LINUX_2
UBUNTU
REDHAT_ENTERPRISE_LINUX
SUSE
CENTOS
ORACLE_LINUX
DEBIAN
    # property : The patch property for which you want to view patch details.
Possible values:

PRODUCT
PRODUCT_FAMILY
CLASSIFICATION
MSRC_SEVERITY
PRIORITY
SEVERITY
    """

    execute_two_parameter("ssm", "describe-patch-properties", "operating-system", "property", parameter_display_string)