#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/define-index-field.html
if __name__ == '__main__':
    """
	delete-index-field : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-index-field.html
	describe-index-fields : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-index-fields.html
    """

    parameter_display_string = """
    # domain-name : A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
    # name : A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.
Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
The name score is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name _id .
    # type : The type of field. The valid options for a field depend on the field type. For more information about the supported field types, see Configuring Index Fields in the Amazon CloudSearch Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudsearch", "define-index-field", "domain-name", "name", "type", add_option_dict)
