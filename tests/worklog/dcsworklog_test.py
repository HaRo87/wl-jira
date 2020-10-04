import pytest
import pandas as pd
import pathlib
import numpy as np
from unittest import TestCase
import tempfile
from wljira.worklog.dcsworklog import _read_dcs_worklog


class TestDCSWorklog(TestCase):
    def test_read_wrong_file_path(self):
        filepath = "/some/path"
        with self.assertLogs() as logs:
            df = _read_dcs_worklog(filepath)
            self.assertEqual(
                logs.output,
                [f"ERROR:wljira.worklog.dcsworklog:Unable to read file: {filepath}"],
            )
            self.assertIsNone(df)

    def test_read_correct_file_path(self):
        entries = [
            [
                "2020-10-04 16:36:29+02:00",
                "2020-10-04 16:36:29+02:00",
                "session",
                "start",
            ],
            [
                "2020-10-04 16:37:50+02:00",
                "2020-10-04 16:37:50+02:00",
                "task",
                "start",
                "test",
            ],
            [
                "2020-10-04 16:50:51+02:00",
                "2020-10-04 16:50:51+02:00",
                "task",
                "stop",
                "test",
            ],
            [
                "2020-10-04 19:54:49+02:00",
                "2020-10-04 19:54:49+02:00",
                "session",
                "start",
            ],
        ]
        df = pd.DataFrame(data=entries)

        tempdir = tempfile.mkdtemp()
        filepath = f"{tempdir}/tests_log"

        df.to_csv(path_or_buf=filepath, sep="|", index=False, header=False)

        with self.assertLogs() as logs:
            df_result = _read_dcs_worklog(filepath)
            self.assertEqual(
                logs.output,
                [f"INFO:wljira.worklog.dcsworklog:Reading file: {filepath}"],
            )
            self.assertTrue(df.equals(df_result))