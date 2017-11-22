# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import getenv
from setuptools import setup


def version():
    if 'TRAVIS_TAG' in sys.environ:
        tag = sys.environ['TRAVIS_TAG']
        if tag.startswith('v'):
            return tag[1:]
        else:
            return tag
    else:
        return "unknown"

setup(
    name='flatbuffers',
    version=version(),
    license='Apache 2.0',
    author='FlatBuffers Contributors',
    author_email='me@rwinslow.com',
    url='https://github.com/google/flatbuffers',
    long_description=('Python runtime library for use with the Flatbuffers'
                      'serialization format.'),
    packages=['flatbuffers'],
    include_package_data=True,
    requires=[],
    description='The FlatBuffers serialization format for Python',
)
