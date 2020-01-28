from acats.base import BaseRecord, Field, BundleBase
from acats.const import ATTransactionType, TransferType, AssetCategory, OptionCategory, RequestedSettlingLocation, \
    RequestedSettlingLocationReason, AssetQuantityRequestIndicator, AssetRequestTransactionCode, PositionCode, \
    BearerBone, CashMarginShortCode, WhenIssuedIndicator, TransferTypeReason


class BaseATRecord(BaseRecord):
    record_type = Field(1, 2, default='AT')


class ATRecord01(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='01')
    logical_sequence_number = Field(5, 6, default='01')
    transaction_type = Field(7, 7, choices=ATTransactionType.keys())
    acats_control_number = Field(8, 21, required=False)
    transfer_type = Field(22, 24, choices=TransferType.keys())
    f1 = Field(25, 28, required=False)
    submitting_participant_number = Field(29, 32, default='0001')
    f2 = Field(33, 36, required=False)
    original_receiver_number = Field(37, 40, default='0001')
    f3 = Field(41, 44, required=False)
    original_deliverer_number = Field(45, 48)
    transaction_reference_id = Field(
        49, 68, required=False, clean_field=lambda x: f'{x.replace("-", "")}'.upper() if x else x
    )
    asset_sequence_number = Field(69, 74, default='000000')
    f4 = Field(75, 76, required=False)
    asset_category = Field(77, 80, required=False, choices=AssetCategory.keys())


class ATRecord02(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='02')
    logical_sequence_number = Field(5, 6, default='02')
    option_category = Field(7, 8, choices=OptionCategory.keys(), default=OptionCategory._00.key)
    requested_settling_location = Field(9, 10, required=False, choices=RequestedSettlingLocation.keys())
    requested_settling_location_reason = Field(11, 14, required=False, choices=RequestedSettlingLocationReason.keys())
    ISIN_country_code = Field(15, 16, required=False, default='US')
    ISIN_security_issue_id = Field(17, 25, required=False)
    ISIN_security_check_digit = Field(26, 26, required=False)
    f1 = Field(27, 80, required=False)


class ATRecord03(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='03')
    logical_sequence_number = Field(5, 6, default='03')
    asset_description_1 = Field(7, 76, required=False)
    f1 = Field(77, 80, required=False)


class ATRecord04(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='04')
    logical_sequence_number = Field(5, 6, default='04')
    asset_description_2 = Field(7, 76, required=False)
    f1 = Field(77, 80, required=False)


class ATRecord05(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='05')
    logical_sequence_number = Field(5, 6, default='05')
    asset_quantity_request_indicator = Field(7, 7, required=False, choices=AssetQuantityRequestIndicator.keys())
    asset_request_transaction_code = Field(8, 8, required=False, choices=AssetRequestTransactionCode.keys())
    asset_quantity = Field(9, 25, required=False)
    asset_percent = Field(26, 40, required=False)
    position_code = Field(41, 41, required=False, choices=PositionCode.keys())
    ISO_currency_code = Field(42, 44, required=False, default='USD')
    asset_amount = Field(45, 61, required=False, clean_field=lambda x: x.replace('.', ','))
    bearer_bond = Field(62, 62, required=False, choices=BearerBone.keys(), default=BearerBone.N.key)
    cash_margin_short_code = Field(63, 63, required=False, choices=CashMarginShortCode.keys())
    when_issued_indicator = Field(64, 64, required=False, choices=WhenIssuedIndicator.keys())
    transfer_type_reason = Field(65, 66, required=False, choices=TransferTypeReason.keys())
    MBS_serial_note = Field(67, 69, required=False)
    f1 = Field(70, 80, required=False)


class ATRecord06(BaseATRecord):
    physical_sequence_number = Field(3, 4, default='06')
    logical_sequence_number = Field(5, 6, default='06')
    asset_comment_1 = Field(7, 66, required=False)
    f1 = Field(67, 80, required=False)


class ATRecord07(BaseATRecord):
    record_type = Field(1, 2, default='AT')
    physical_sequence_number = Field(3, 4, default='97')
    logical_sequence_number = Field(5, 6, default='07')
    asset_comment_2 = Field(7, 66, required=False)
    f1 = Field(67, 80, required=False)


class ATRecordBundle(BundleBase):
    bundle_class = [ATRecord01, ATRecord02, ATRecord03, ATRecord04, ATRecord05, ATRecord06, ATRecord07]

    def __init__(
        self,
        at_record_01: ATRecord01,
        at_record_02: ATRecord02,
        at_record_03: ATRecord03,
        at_record_04: ATRecord04,
        at_record_05: ATRecord05,
        at_record_06: ATRecord06,
        at_record_07: ATRecord07,
    ):
        self.at_record_01 = at_record_01
        self.at_record_02 = at_record_02
        self.at_record_03 = at_record_03
        self.at_record_04 = at_record_04
        self.at_record_05 = at_record_05
        self.at_record_06 = at_record_06
        self.at_record_07 = at_record_07
