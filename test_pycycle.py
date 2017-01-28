from __future__ import print_function
import os
import pytest

import pycycle.utils


def test_get_path_from_package_name():
    pass


def test_format_path():
    pass


def test_simple_project():
    project = {'path': os.path.abspath('./tests/_projects/a_references_b_b_references_a'),
               'has_cycle': True,
               'result': 'b_module: Line 1 -> a_module: Line 2 =>> b_module'}

    root_node = pycycle.utils.read_project(project['path'])
    assert root_node != None
    assert pycycle.utils.check_if_cycles_exist(
        root_node) == project['has_cycle']
    assert pycycle.utils.get_cycle_path(root_node) == project['result']


def test_no_circular_imports():
    project = {'path': os.path.abspath('./tests/_projects/has_no_circular_imports'),
               'has_cycle': False,
               'result': ''}
    root_node = pycycle.utils.read_project(project['path'])
    assert root_node != None
    assert pycycle.utils.check_if_cycles_exist(
        root_node) == project['has_cycle']
    assert pycycle.utils.get_cycle_path(root_node) == ''


def test_large_circle():
    project = {'path': os.path.abspath('./tests/_projects/large_circle'),
               'has_cycle': True,
               'result': 'a_module.a_file: Line 1 -> a_module.b_module.b_file: Line 1 -> c_module.c_file: Line 1 -> d_module.d_file: Line 1 =>> a_module.a_file'}

    root_node = pycycle.utils.read_project(project['path'])
    assert root_node != None
    assert pycycle.utils.check_if_cycles_exist(
        root_node) == project['has_cycle']
    assert pycycle.utils.get_cycle_path(root_node) == project['result']