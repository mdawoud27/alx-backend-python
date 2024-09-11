#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)
