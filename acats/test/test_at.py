import unittest

from acats.asset_input import ATRecord01, ATRecord02, ATRecord03, ATRecord04, ATRecord05, ATRecord06, ATRecord07, \
    ATRecordBundle
from acats.const import ATTransactionType, TransferType, AssetCategory, RequestedSettlingLocation, \
    AssetQuantityRequestIndicator, AssetRequestTransactionCode, PositionCode, CashMarginShortCode, WhenIssuedIndicator


class TestATRecord(unittest.TestCase):

    def test_generate_at_record(self):
        at1 = ATRecord01(
            transaction_type=ATTransactionType.A.key,
            transfer_type=TransferType.PTR.key,
            original_deliverer_number='0534',
            transaction_reference_id='UUUU0001234',
            asset_sequence_number='0',
            asset_category=AssetCategory.EQU.key
        )
        at2 = ATRecord02(
            requested_settling_location=RequestedSettlingLocation._00.key,
            ISIN_security_issue_id='AAPL'
        )
        at3 = ATRecord03()
        at4 = ATRecord04()
        at5 = ATRecord05(
            asset_quantity_request_indicator=AssetQuantityRequestIndicator.P.key,
            asset_request_transaction_code=AssetRequestTransactionCode._2.key,
            asset_quantity='100',
            position_code=PositionCode.L.key,
            cash_margin_short_code=CashMarginShortCode.M.key,
            when_issued_indicator=WhenIssuedIndicator.W.key,
        )
        at6 = ATRecord06()
        at7 = ATRecord07()
        at = ATRecordBundle(at1, at2, at3, at4, at5, at6, at7)
        s = 'AT0101A              PTR    0001    0001    0534UUUU0001234         0       EQU \r\n' \
            'AT02020000    USAAPL                                                            \r\n' \
            'AT0303                                                                          \r\n' \
            'AT0404                                                                          \r\n' \
            'AT0505P2100                             LUSD                 NMW                \r\n' \
            'AT0606                                                                          \r\n' \
            'AT9707                                                                          \r\n'
        self.assertEqual(s, at.generate_bundle_str())
