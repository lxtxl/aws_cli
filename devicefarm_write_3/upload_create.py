#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html
if __name__ == '__main__':
    """
	delete-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-upload.html
	get-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html
	list-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-uploads.html
	update-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-upload.html
    """

    parameter_display_string = """
    # project-arn : The ARN of the project for the upload.
    # name : The uploadâs file name. The name should not contain any forward slashes (/ ). If you are uploading an iOS app, the file name must end with the .ipa extension. If you are uploading an Android app, the file name must end with the .apk extension. For all others, the file name must end with the .zip file extension.
    # type : The uploadâs upload type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC

If you call CreateUpload with WEB_APP specified, AWS Device Farm throws an ArgumentException error.
Possible values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("devicefarm", "create-upload", "project-arn", "name", "type", add_option_dict)
