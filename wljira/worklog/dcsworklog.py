import logging
import os
import pandas as pd

DEFAULT_SEPARATOR = "|"

logger = logging.getLogger(__name__)


def _read_dcs_worklog(path):
    _log_df = None
    if os.path.exists(path):
        logger.info(f"Reading file: {path}")
        _log_df = pd.read_csv(
            filepath_or_buffer=path, sep=DEFAULT_SEPARATOR, header=None
        )
    else:
        logger.error(f"Unable to read file: {path}")

    return _log_df
