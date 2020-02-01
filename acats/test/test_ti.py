import unittest

from acats.transfer_input import TIRecord01, TIRecord02, TIRecord03, TIRecord04, TIRecord05, TIRecordBundle


class TestTIRecord(unittest.TestCase):

    def test_generate_ti_record(self):
        ti1 = TIRecord01(
            transaction_type='A',
            transfer_type='FUL',
            original_deliverer_number='0534',
            original_receiver_customer_account_number='SSTSXCTD-00001234'
        )
        s = 'TI0101A              FUL    0873    0873    0534SSTSSSTSXCTD00001234            \r\n'
        # print(ti1.convert_str_to_dict(s))
        self.assertEqual(ti1.generate_value_str(), s)

    def test_generate_ti_record_bundle(self):
        ti1 = TIRecord01(
            transaction_type='A',
            transfer_type='FUL',
            original_deliverer_number='0534',
            original_receiver_customer_account_number='XCTD-00001234'
        )
        ti2 = TIRecord02(
            original_receiver_customer_account_name='MINJIN CHEN',
            original_receiver_customer_ssn_or_tax_id_primary='000000000'
        )
        ti3 = TIRecord03(
            original_receiver_customer_account_type='SN',
            original_deliverer_customer_account_number='U8517898'
        )
        ti4 = TIRecord04(transaction_reference_id=None)
        ti5 = TIRecord05()

        ti = TIRecordBundle(ti1, ti2, ti3, ti4, ti5)
        r = "TI0101A              FUL    0873    0873    0534SSTSXCTD00001234                \r\n" \
            "TI0202MINJIN CHEN                                                 000000000     \r\n" \
            "TI0303         SN            SSTS    U8517898                                   \r\n" \
            "TI0404                                                                          \r\n" \
            "TI9505                                                                          \r\n"
        self.assertEqual(ti.generate_bundle_str(), r)
        # reverse conversion
        ti = TIRecordBundle.new_instance_from_text(
            ti.generate_bundle_str(),
            keys=['record_type', 'physical_sequence_number', 'logical_sequence_number']
        )
        # print(ti.generate_list_of_dict())
        self.assertEqual(ti.generate_bundle_str(), r)
