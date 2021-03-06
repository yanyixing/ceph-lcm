# -*- coding: utf-8 -*-
# Copyright (c) 2016 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Different utilities related to the time."""


import datetime

import time


def current_unix_timestamp():
    """Returns a current UNIX timestamp (in seconds, ms are truncated)."""

    return int(time.time())


def timer():
    """Returns a timer with second precision. This is not UNIX time,
    this is monotonic timer which is indifferent to changes of system
    clock.
    """

    return int(time.monotonic())


def datenow():
    return datetime.datetime.utcnow().replace(microsecond=0)


def ttl(offset):
    if not isinstance(offset, datetime.timedelta):
        offset = datetime.timedelta(seconds=int(offset))

    return datenow() + offset


def keystone_to_utc(data):
    dtime = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%fZ")
    dtime = dtime.replace(tzinfo=datetime.timezone.utc)

    return dtime
