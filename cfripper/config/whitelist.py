"""
Copyright 2018 Skyscanner Ltd

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import re
from typing import List

"""
A list of projects that are allowed to skip specific checks.

The format:

whitelist = {
    "stack_name1": [
        "RULE2",
        "RULE3",
    ],
    "stack_name2": [
        "RULE2",
        "RULE3",
    ]
}

"""
stack_whitelist = {}

"""
A list of resources that are allowed to use wildcard principals, grouped by stack name

The format:

wildcard_principal_resource_whitelist = {
    "stack_name1": [
        "RESOURCE_NAME_1",
        "RESOURCE_NAME_2",
    ],
    "stack_name2": [
        "RESOURCE_NAME_3",
        "RESOURCE_NAME_4",
    ]
}

"""

wildcard_principal_resource_whitelist = {}


def get_stack_exemption_list(stack_name) -> List[str]:
    for k, v in stack_whitelist.items():
        if re.match(k, stack_name):
            return v

    return []


def get_wildcard_principal_exemption_resource_list(stack_name) -> List[str]:

    allowed_resources = []
    for k, v in wildcard_principal_resource_whitelist.items():
        if re.match(k, stack_name):
            allowed_resources += v

    return allowed_resources
