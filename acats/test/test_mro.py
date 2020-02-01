import unittest

from acats.mro import MROTransferOutputBundle, MROAssetOutputBundle


class TestMRORecord(unittest.TestCase):

    def test_generate_mro_mt_cls(self):
        text = 'MT0101B201935400420660000002019122003    00011  100001                          \r\n' \
               'MT02020000000000000 0  0     2                                        TI03560101\r\n' \
               'MT0303A20193540042066FUL    0001    0001    0534XXXXXCTD00010024                \r\n' \
               'MT0404NAME NAME                                                   000000000     \r\n' \
               'MT0505         SN0                  2U0000000                                   \r\n' \
               'MT0606                                                                          \r\n' \
               'MT9707                                                                          \r\n'
        mro_mt = MROTransferOutputBundle.new_instance_from_text(
            text,
            keys=['record_type', 'record_subtype', 'physical_sequence_number', 'logical_sequence_number']
        )
        self.assertEqual(mro_mt.generate_bundle_str(), text)

    def test_generate_mro_ma_cls(self):
        text_1 = 'MA0101B201935400420660000022019122302    08733  200001                          \r\n' \
                 'MA02020000000000 0002 0022  0 002000  0                               AT04310101\r\n' \
                 'MA0303A20193540042066FUL    0534    0001    0534                    000002EQU   \r\n' \
                 'MA04040005    US0079031078                                                      \r\n' \
                 'MA0505ADVANCED MICRO DEVICES INC    COM                                         \r\n' \
                 'MA0606                                                                          \r\n' \
                 'MA0707  00000000000000018               LUSD00000000000794,70NCN                \r\n' \
                 'MA0808t2                                                                        \r\n' \
                 'MA9909                                                                          \r\n'
        mro_ma = MROAssetOutputBundle.new_instance_from_text(
            text_1,
            keys=['record_type', 'record_subtype', 'physical_sequence_number', 'logical_sequence_number']
        )
        self.assertEqual(mro_ma.generate_bundle_str(), text_1)
        text_2 = 'MA0101B201935400420660000012019122302    08733  200001                          \r\n' \
                 'MA02020000000000 0 0002  2    200 0   0                               AT04310101\r\n' \
                 'MA0303A20193540042066FUL    0534    0873    0534                    000001      \r\n' \
                 'MA04040040CRED                                                                  \r\n' \
                 'MA0505CREDIT CASH BALANCE                                                       \r\n' \
                 'MA0606                                                                          \r\n' \
                 'MA0707  00000000000000000                USD00000000000038,07 C                 \r\n' \
                 'MA0808t1                                                                        \r\n' \
                 'MA9909                                                                          \r\n'
        mro_ma = MROAssetOutputBundle.new_instance_from_text(
            text_2,
            keys=['record_type', 'record_subtype', 'physical_sequence_number', 'logical_sequence_number']
        )
        self.assertEqual(mro_ma.generate_bundle_str(), text_2)
