#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/upgrade-elasticsearch-domain.html
if __name__ == '__main__':
    """
	create-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-elasticsearch-domain.html
	delete-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-elasticsearch-domain.html
	describe-elasticsearch-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain.html
	describe-elasticsearch-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domains.html
    """

    parameter_display_string = """
    # domain-name : The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
    # target-version : The version of Elasticsearch that you intend to upgrade the domain to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("es", "upgrade-elasticsearch-domain", "domain-name", "target-version", add_option_dict)
