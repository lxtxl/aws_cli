#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/associate-external-connection.html
if __name__ == '__main__':
    """
	disassociate-external-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/disassociate-external-connection.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository.
    # repository : The name of the repository to which the external connection is added.
    # external-connection : The name of the external connection to add to the repository. The following values are supported:

public:npmjs - for the npm public repository.
public:pypi - for the Python Package Index.
public:maven-central - for Maven Central.
public:maven-googleandroid - for the Google Android repository.
public:maven-gradleplugins - for the Gradle plugins repository.
public:maven-commonsware - for the CommonsWare Android repository.
public:nuget-org - for the NuGet Gallery.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeartifact", "associate-external-connection", "domain", "repository", "external-connection", add_option_dict)
