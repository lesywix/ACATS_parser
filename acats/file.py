from datetime import datetime
from typing import List

import pytz

from acats.asset_input import ATRecordBundle
from acats.header_trailer import Header, Trailer
from acats.transfer_input import TIRecordBundle


def get_timezone_now(timezone='UTC'):
    """
    need set USE_TZ = True in settings
    :timezone: str of timezone
    :return: datetime now determined by timezone in django
    """
    value = datetime.now()
    timezone = pytz.timezone(timezone)
    return value.astimezone(timezone)


def generate_32667_file(
    multi_batch_number: str,
    ti: TIRecordBundle,
    at_equities: List[ATRecordBundle] = None,
    at_cash: List[ATRecordBundle] = None
):
    est_now = get_timezone_now('EST')
    header = Header(submission_date=est_now.strftime("%m%d%Y"), multi_batch_number=multi_batch_number)
    trailer = Trailer()
    with open(f'SSTS_NSCC_32667_{est_now.strftime("%y%m%d")}_{multi_batch_number}.txt', 'w') as f:
        f.writelines(header.generate_value_str())
        f.writelines(ti.generate_bundle_str())
        if at_equities:
            for i in at_equities:
                f.writelines(i.generate_bundle_str())
        if at_cash:
            for i in at_cash:
                f.writelines(i.generate_bundle_str())
        f.writelines(trailer.generate_value_str(with_line_break=False))
    return f


def generate_32667_file_content(
    submission_date: datetime,
    multi_batch_number: str,
    transfer_inputs: str,
    asset_inputs: str
) -> (str, str):
    """
    :param submission_date:
    :param multi_batch_number:
    :param transfer_inputs: AcatsTransferRequest object.transfer_inputs
    :param asset_inputs: AcatsTransferRequest object.asset_inputs
    :return: filename, content
    """
    filename = f'SSTS_NSCC_32667_{submission_date.strftime("%y%m%d")}_{multi_batch_number:03}.txt'
    header = Header(submission_date=submission_date.strftime("%m%d%Y"), multi_batch_number=multi_batch_number)
    trailer = Trailer()
    content = (
        header.generate_value_str()
        + transfer_inputs +
        asset_inputs +
        trailer.generate_value_str(with_line_break=False)
    )
    return filename, content
