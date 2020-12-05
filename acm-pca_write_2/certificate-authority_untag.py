#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html
if __name__ == '__main__':
    """
	create-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html
	delete-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html
	describe-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html
	list-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html
	restore-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/restore-certificate-authority.html
	tag-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html
	update-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``
    # tags : List of tags to be removed from the CA.
(structure)

Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the TagCertificateAuthority action. To remove a tag, call the UntagCertificateAuthority action.
Key -> (string)

Key (name) of the tag.

Value -> (string)

Value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm-pca", "untag-certificate-authority", "certificate-authority-arn", "tags", add_option_dict)
