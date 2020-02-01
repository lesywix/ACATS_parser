from acats.base import BaseRecord, Field, BundleBase
from acats.const import TransferType, TITransactionType, OriginalReceiverCustomerAccountType, TransferTypeReject


class BaseTIRecord(BaseRecord):
    record_type = Field(1, 2, default='TI')


class TIRecord01(BaseTIRecord):
    physical_sequence_number = Field(3, 4, default='01')
    logical_sequence_number = Field(5, 6, default='01')
    transaction_type = Field(7, 7, choices=TITransactionType.keys())
    acats_control_number = Field(8, 21, required=False)
    transfer_type = Field(22, 24, choices=TransferType.keys())
    f1 = Field(25, 28, required=False)
    submitting_participant_number = Field(29, 32)
    f2 = Field(33, 36, required=False)
    original_receiver_number = Field(37, 40)
    f3 = Field(41, 44, required=False)
    original_deliverer_number = Field(45, 48)
    original_receiver_customer_account_number = Field(
        49, 68
    )
    f4 = Field(69, 80, required=False)


class TIRecord02(BaseTIRecord):
    physical_sequence_number = Field(3, 4, default='02')
    logical_sequence_number = Field(5, 6, default='02')
    original_receiver_customer_account_name = Field(7, 66, required=False)
    original_receiver_customer_ssn_or_tax_id_primary = Field(67, 75, required=False)
    f1 = Field(76, 80, required=False)


class TIRecord03(BaseTIRecord):
    physical_sequence_number = Field(3, 4, default='03')
    logical_sequence_number = Field(5, 6, default='03')
    original_receiver_customer_ssn_or_tax_id_secondary = Field(7, 15, required=False)
    original_receiver_customer_account_type = Field(
        16, 17, required=False, choices=OriginalReceiverCustomerAccountType.keys()
    )
    gift_or_donation_indicator = Field(18, 18, required=False, choices=['0', '1'])
    f1 = Field(19, 20, required=False)
    original_receiver_occ_broker_number = Field(21, 25, required=False)
    f2 = Field(26, 29, required=False)
    original_receiver_correspondent = Field(30, 33, default='XXXX')
    f3 = Field(34, 37, required=False)
    original_deliverer_customer_account_number = Field(
        38, 57, required=False, clean_field=lambda x: x.upper() if x else x
    )
    transfer_type_reject = Field(58, 59, required=False, choices=TransferTypeReject.keys())
    associated_acats_control_number = Field(60, 73, required=False)
    f4 = Field(74, 80, required=False)


class TIRecord04(BaseTIRecord):
    physical_sequence_number = Field(3, 4, default='04')
    logical_sequence_number = Field(5, 6, default='04')
    associated_settlement_date = Field(7, 14, required=False)
    transaction_reference_id = Field(
        15, 34, required=False
    )
    comments_1 = Field(35, 80, required=False)


class TIRecord05(BaseTIRecord):
    physical_sequence_number = Field(3, 4, default='95')
    logical_sequence_number = Field(5, 6, default='05')
    comments_2 = Field(7, 80, required=False)


class TIRecordBundle(BundleBase):
    bundle_class = [TIRecord01, TIRecord02, TIRecord03, TIRecord04, TIRecord05]

    def __init__(self, ti_record_01: TIRecord01, ti_record_02: TIRecord02, ti_record_03: TIRecord03,
                 ti_record_04: TIRecord04, ti_record_05: TIRecord05):
        self.ti_record_01 = ti_record_01
        self.ti_record_02 = ti_record_02
        self.ti_record_03 = ti_record_03
        self.ti_record_04 = ti_record_04
        self.ti_record_05 = ti_record_05
