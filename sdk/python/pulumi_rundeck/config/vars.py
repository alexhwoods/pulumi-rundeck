# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'api_version',
    'auth_token',
    'url',
]

__config__ = pulumi.Config('rundeck')

api_version = __config__.get('apiVersion')
"""
API Version of the target Rundeck server.
"""

auth_token = __config__.get('authToken')
"""
Auth token to use with the Rundeck API.
"""

url = __config__.get('url')
"""
URL of the root of the target Rundeck server.
"""

