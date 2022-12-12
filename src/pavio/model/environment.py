# MIT License
#
# Copyright (c) 2023 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Environment:
    """Environment Model"""

    def __init__(self, id, name, path, tags, created_at, updated_at):
        """Class Constructor"""
        self._id = id
        self._name = name
        self._path = path
        self._tags = tags
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """Environment ID"""
        return self._id

    @property
    def name(self):
        """Environment Name"""
        return self._name

    @property
    def path(self):
        """Environment Path"""
        return self._path

    @property
    def tags(self):
        """Environment Tags"""
        return self._tags

    @property
    def created_at(self):
        """Environment Created At"""
        return self._created_at

    @property
    def updated_at(self):
        """Environment Updated At"""
        return self._updated_at
