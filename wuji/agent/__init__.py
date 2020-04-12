"""
Copyright (C) 2018--2020, 申瑞珉 (Ruimin Shen)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import functools

import wuji


def make(config, context, kind, blob=None):
    module = functools.reduce(lambda x, wrap: wrap(x), map(wuji.parse.instance, context['module']))
    model = module(config, **context['init'][kind]['kwargs'])
    if blob is not None:
        model.set_blob(blob)
    return functools.reduce(lambda x, wrap: wrap(x), map(wuji.parse.instance, context['agent']['eval']))(model)
