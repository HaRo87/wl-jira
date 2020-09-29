import pytest
from click.testing import CliRunner
from unittest import TestCase

from wljira.wljira import cli


class TestWLJira(TestCase):
    def test_info(self):
        runner = CliRunner()
        result = runner.invoke(cli, "info")
        output = "Thanks for using wlj!"
        self.assertEqual(result.exit_code, 0)
        self.assertIn(output, result.output)