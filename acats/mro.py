from acats.base import BaseRecord, Field, BundleBase


# Transfer Output #


class MROTransferOutput01(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='01')
    logical_sequence_number = Field(5, 6, default='01')
    distribution_side = Field(7, 7)
    acats_control_number = Field(8, 21)
    asset_sequence_number = Field(22, 27)
    processing_date = Field(28, 35)
    cycle = Field(36, 37)
    f1 = Field(38, 41)
    distribution_participant = Field(42, 45)
    system_action = Field(46, 46)
    system_reject_reason = Field(47, 48)
    status = Field(49, 51)
    days_in_status = Field(52, 54)
    f2 = Field(55, 72)
    registration_indicator = Field(73, 73)
    f3 = Field(74, 80)


class MROTransferOutput02(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='02')
    logical_sequence_number = Field(5, 6, default='02')
    ti_record_type_status = Field(7, 7)
    ti_record_length_status = Field(8, 8)
    ti_physical_sequence_number_status = Field(9, 9)
    ti_logical_sequence_number_status = Field(10, 10)
    ti_transaction_type_status = Field(11, 11)
    ti_acats_control_number_status = Field(12, 12)
    ti_transfer_type = Field(13, 13)
    ti_submitting_participant_number_status = Field(14, 14)
    ti_original_receiver_number_status = Field(15, 15)
    ti_original_deliverer_number_status = Field(16, 16)
    original_receiver_customer_account_number_status = Field(17, 17)
    original_receiver_customer__account_name_status = Field(18, 18)
    original_receiver_status_customer_ss_number_or_tax_id_primary_status = Field(19, 19)
    original_receiver_customer_ss_number_or_tax_id_secondary_status = Field(20, 20)
    original_receiver_customer_account_type_status = Field(21, 21)
    original_receiver__occ_broker_number_status = Field(22, 22)
    original_receiver_correspondent_status = Field(23, 23)
    original_deliverer_customer_account_number_status = Field(24, 24)
    transfer_type_reject_status = Field(25, 25)
    associated_acats_control_number_status = Field(26, 26)
    associated_settlement_date_status = Field(27, 27)
    ti_transaction_reference_id_status = Field(28, 28)
    comments_status = Field(29, 29)
    gift_or_donation_indicator_status = Field(30, 30)
    f1 = Field(31, 70)
    ti_record_type = Field(71, 72)
    ti_record_length = Field(73, 76)
    ti_physical_sequence_number = Field(77, 78)
    ti_logical_sequence_number = Field(79, 80)


class MROTransferOutput03(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='03')
    logical_sequence_number = Field(5, 6, default='03')
    transaction_type = Field(7, 7)
    acats_control_number = Field(8, 21)
    transfer_type = Field(22, 24)
    f1 = Field(25, 28)
    submitting_participant_number = Field(29, 32)
    f2 = Field(33, 36)
    original_receiver_number = Field(37, 40)
    f3 = Field(41, 44)
    original_deliverer_number = Field(45, 48)
    original_receiver_customer_account_number = Field(49, 68)
    f4 = Field(69, 80)


class MROTransferOutput04(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='04')
    logical_sequence_number = Field(5, 6, default='04')
    original_receiver_customer_account_name = Field(7, 66)
    original_receiver_customer_ss_number_or_tax_id_primary = Field(67, 75)
    f1 = Field(76, 80)


class MROTransferOutput05(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='05')
    logical_sequence_number = Field(5, 6, default='05')
    original_receiver_customer_ss_number_or_tax_id_secondary = Field(7, 15)
    original_receiver_customer_account_type = Field(16, 17)
    gift_or_donation_indicator = Field(18, 18)
    f1 = Field(19, 20)
    original_receiver_occ_broker_number = Field(21, 25)
    f2 = Field(26, 29)
    original_receiver_correspondent = Field(30, 33)
    f3 = Field(34, 36)
    contra_participant_type = Field(37, 37)
    original_deliverer_customer_account_number = Field(38, 57)
    transfer_type_reject = Field(58, 59)
    associated_acats_control_number = Field(60, 73)
    f4 = Field(74, 80)


class MROTransferOutput06(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='06')
    logical_sequence_number = Field(5, 6, default='06')
    associated_settlement_date = Field(7, 14)
    ti_transaction_reference_id = Field(15, 34)
    comments_1 = Field(35, 80)


class MROTransferOutput07(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='T')
    physical_sequence_number = Field(3, 4, default='97')
    logical_sequence_number = Field(5, 6, default='07')
    comments_2 = Field(7, 80)


class MROTransferOutputBundle(BundleBase):
    bundle_class = [
        MROTransferOutput01, MROTransferOutput02, MROTransferOutput03, MROTransferOutput04,
        MROTransferOutput05, MROTransferOutput06, MROTransferOutput07
    ]

    def __init__(self, *args, **kwargs):
        for v in args:
            setattr(self, v.__class__.__name__, v)
        for k, v in kwargs.items():
            setattr(self, k, v)

# Asset Output #


class MROAssetOutput01(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='01')
    logical_sequence_number = Field(5, 6, default='01')
    distribution_side = Field(7, 7)
    acats_control_number = Field(8, 21)
    asset_sequence_number = Field(22, 27)
    processing_date = Field(28, 35)
    cycle = Field(36, 37)
    f1 = Field(38, 41)
    distribution_participant = Field(42, 45)
    system_action = Field(46, 46)
    system_reject_reason = Field(47, 48)
    status = Field(49, 51)
    days_in_status = Field(52, 54)
    f2 = Field(55, 72)
    registration_indicator = Field(73, 73)
    f3 = Field(74, 80)


class MROAssetOutput02(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='02')
    logical_sequence_number = Field(5, 6, default='02')
    at_record_type_status = Field(7, 7)
    at_record_length_status = Field(8, 8)
    at_physical_sequence_number_status = Field(9, 9)
    at_logical_sequence_number_status = Field(10, 10)
    at_transaction_type_status = Field(11, 11)
    at_acats_control_number_status = Field(12, 12)
    at_transfer_type_status = Field(13, 13)
    at_submitting_participant_number_status = Field(14, 14)
    at_original_receiver_number_status = Field(15, 15)
    at_original_deliverer__number_status = Field(16, 16)
    at_transaction_reference_id_status = Field(17, 17)
    at_asset_sequence_number_status = Field(18, 18)
    asset_pricing_category_status = Field(19, 19)
    option_category_status = Field(20, 20)
    settling_location__status = Field(21, 21)
    settling_location__reason_status = Field(22, 22)
    isin_country_code_status = Field(23, 23)
    isin_security_issue_id_status = Field(24, 24)
    isin_security_check_digit__status = Field(25, 25)
    asset_description_status = Field(26, 26)
    asset_quantity_request_indicator_status = Field(27, 27)
    asset_request_transaction_code_status = Field(28, 28)
    asset_quantity_status = Field(29, 29)
    asset_percent_status = Field(30, 30)
    position_code_status = Field(31, 31)
    iso_currency_code_status = Field(32, 32)
    asset_amount_status = Field(33, 33)
    bearer_bond_status = Field(34, 34)
    cash_margin_short_code_status = Field(35, 35)
    when_issued_indicator_status = Field(36, 36)
    transfer_type_reason_status = Field(37, 37)
    mbs_serial_note_status = Field(38, 38)
    asset_comment_status = Field(39, 39)
    option_buy_sell_indicator_status = Field(40, 40)
    option_p_c_indicator_status = Field(41, 41)
    option_o_c_indicator_status = Field(42, 42)
    option_symbol_status = Field(43, 43)
    option_expiration_date_status = Field(44, 44)
    option_strike_price_integer__status = Field(45, 45)
    option_strike_price_fraction_status = Field(46, 46)
    option_occ_deliverer_number_status = Field(47, 47)
    option_account_type_status = Field(48, 48)
    sub_account_id_status = Field(49, 49)
    option_comments_status = Field(50, 50)
    fund_customer_account_number_status = Field(51, 51)
    book_or_physical_share_indicator_status = Field(52, 52)
    network_control_indicator_status = Field(53, 53)
    account_type_indicator_status = Field(54, 54)
    dividend_code_status = Field(55, 55)
    dividend_payee_indicator_status = Field(56, 56)
    executing_broker_status = Field(57, 57)
    mf_full_or_partial_indicator_status = Field(58, 58)
    share_aging_indicator_status = Field(59, 59)
    firm_membership_indicator_deliverer_status = Field(60, 60)
    new_fund_customer_account_number_receiver_status = Field(61, 61)
    re_registration_date_at_fund_status = Field(62, 62)
    mf_agent_processing_indicator_deliverer_status = Field(63, 63)
    f1 = Field(64, 70)
    at_record_type = Field(71, 72)
    at_record_length = Field(73, 76)
    at_physical_sequence_number = Field(77, 78)
    at_logical_sequence_number = Field(79, 80)


class MROAssetOutput03(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='03')
    logical_sequence_number = Field(5, 6, default='03')
    at_transaction_type = Field(7, 7)
    at_acats_control_number = Field(8, 21)
    at_transfer_type = Field(22, 24)
    f1 = Field(25, 28)
    at_submitting_participant_number = Field(29, 32)
    f2 = Field(33, 36)
    at_original_receiver_number = Field(37, 40)
    f3 = Field(41, 44)
    at_original_deliverer_number = Field(45, 48)
    at_transaction_reference_id = Field(49, 68)
    at_asset_sequence_number = Field(69, 74)
    asset_pricing_category = Field(75, 78)
    f4 = Field(79, 80)


class MROAssetOutput04(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='04')
    logical_sequence_number = Field(5, 6, default='04')
    option_category = Field(7, 8)
    settling_location = Field(9, 10)
    settling_location_reason = Field(11, 14)
    isin_country_code = Field(15, 16)
    isin_security_issue_id = Field(17, 25)
    isin_security_check_digit = Field(26, 26)
    dtc_sub_issue_type = Field(27, 27)
    f1 = Field(28, 80)


class MROAssetOutput05(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='05')
    logical_sequence_number = Field(5, 6, default='05')
    asset_description_1 = Field(7, 76)
    f1 = Field(77, 80)


class MROAssetOutput06(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='06')
    logical_sequence_number = Field(5, 6, default='06')
    asset_description_2 = Field(7, 76)
    f1 = Field(77, 80)


class MROAssetOutput07(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='07')
    logical_sequence_number = Field(5, 6, default='07')
    asset_quantity_request_indicator = Field(7, 7)
    asset_request_transaction_code = Field(8, 8)
    asset_quantity = Field(9, 25)
    asset_percent = Field(26, 40)
    position_code = Field(41, 41)
    iso_currency_code = Field(42, 44)
    asset_amount = Field(45, 61)
    bearer_bond = Field(62, 62)
    cash_margin_short_code = Field(63, 63)
    when_issued_indicator = Field(64, 64)
    transfer_type_reason = Field(65, 66)
    mbs_serial_note = Field(67, 69)
    f1 = Field(70, 80)


class MROAssetOutput08(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='08')
    logical_sequence_number = Field(5, 6, default='08')
    asset_comment_1 = Field(7, 66)
    f1 = Field(67, 80)


class MROAssetOutput09(BaseRecord):
    record_type = Field(1, 1, default='M')
    record_subtype = Field(2, 2, default='A')
    physical_sequence_number = Field(3, 4, default='99')
    logical_sequence_number = Field(5, 6, default='09')
    asset_comment_2 = Field(7, 66)
    f1 = Field(67, 80)


class MROAssetOutputBundle(BundleBase):
    bundle_class = [
        MROAssetOutput01, MROAssetOutput02, MROAssetOutput03, MROAssetOutput04,
        MROAssetOutput05, MROAssetOutput06, MROAssetOutput07, MROAssetOutput08, MROAssetOutput09,
    ]

    def __init__(self, *args, **kwargs):
        for v in args:
            setattr(self, v.__class__.__name__, v)
        for k, v in kwargs.items():
            setattr(self, k, v)

# NOT SUPPORTED
# class MROAssetOutput10(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4, default='10')
#     logical_sequence_number = Field(5, 6, default='10')
#     option_buy_sell_indicator = Field(7, 7)
#     option_p_c_indicator = Field(8, 8)
#     option_o_c_indicator = Field(9, 9)
#     option_symbol = Field(10, 15)
#     option_expiration_date = Field(16, 23)
#     f1 = Field(24, 29)
#     option_decimal_or_fraction_indicator = Field(30, 30)
#     option_strike_price_integer = Field(31, 35)
#     f2 = Field(36, 37)
#     option_strike_price_decimal = Field(38, 40)
#     f3 = Field(41, 42)
#     option_occ_deliverer_number = Field(43, 47)
#     option_account_type = Field(48, 48)
#     f4 = Field(49, 52)
#     sub_account_id = Field(53, 56)
#     option_comments = Field(57, 72)
#     f5 = Field(73, 80)
#
#
# class MROAssetOutput11(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4, default='11')
#     logical_sequence_number = Field(5, 6, default='10')
#     fund_customer_account_number = Field(7, 26)
#     book_or_physical_share_indicator = Field(27, 27)
#     network_control_indicator = Field(28, 28)
#     account_type_indicator = Field(29, 29)
#     dividend_code = Field(30, 30)
#     dividend_payee_indicator = Field(31, 31)
#     f1 = Field(32, 35)
#     executing_broker = Field(36, 39)
#     mf_full_or_partial_indicator = Field(40, 40)
#     share_aging_indicator = Field(41, 41)
#     firm_membership_indicator_deliverer = Field(42, 43)
#     new_fund_customer_account_number_receiver = Field(44, 63)
#     re_registration_date_at_fund = Field(64, 71)
#     mf_agent_processing_indicator = Field(72, 72)
#     f2_asset_insurance_data = Field(73, 80)
#
#
# class MROAssetOutput12(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4, default='12')
#     logical_sequence_number = Field(5, 6, default='10')
#     insurance_customer_account_number_deliverer_status = Field(7, 7)
#     owner_1_natural_or_non_natural_indicator_status = Field(8, 8)
#     owner_1_name_status = Field(9, 9)
#     owner_1_id__status = Field(10, 10)
#     owner_1_id_qualifier_status = Field(11, 11)
#     owner_1_qualifier_status = Field(12, 12)
#     owner_2_natural_or_non_natural_indicator_status = Field(13, 13)
#     owner_2_name_status = Field(14, 14)
#     owner_2_id_status = Field(15, 15)
#     owner_2_id_qualifier_status = Field(16, 16)
#     owner_2_qualifier_status = Field(17, 17)
#     annuitant_1_name_status = Field(18, 18)
#     annuitant_1_id_status = Field(19, 19)
#     annuitant_1_id_qualifier_status = Field(20, 20)
#     annuitant_2_name_status = Field(21, 21)
#     annuitant_2_id_status = Field(22, 22)
#     annuitant_2_id_qualifier_status = Field(23, 23)
#     irs_qualification_code_status = Field(24, 24)
#     contract_number_status = Field(25, 25)
#     contract_value_status = Field(26, 26)
#     contract_value_as_of_date_status = Field(27, 27)
#     delivering_associated_firm_id_status = Field(28, 28)
#     f1 = Field(29, 80)
#
#
# class MROAssetOutput13(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='11')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput14(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='12')
#     insurance_customer_account_number_deliverer = Field(7, 26)
#     owner_1_natural_non_natural_indicator = Field(27, 27)
#     owner_1_name_1 = Field(28, 77)
#     f1 = Field(78, 80)
#
#
# class MROAssetOutput15(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='13')
#     owner_1_name_2 = Field(7, 61)
#     f1 = Field(62, 80)
#
#
# class MROAssetOutput16(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='14')
#     owner_1_id = Field(7, 26)
#     owner_1_id_qualifier = Field(27, 28)
#     owner_1_qualifier = Field(29, 29)
#     f1 = Field(30, 80)
#
#
# class MROAssetOutput17(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='15')
#     owner_2_natural_or_non_natural_indicator = Field(7, 7)
#     owner_2_name_1 = Field(8, 57)
#     f1 = Field(58, 80)
#
#
# class MROAssetOutput18(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='16')
#     owner_2_name_2 = Field(7, 61)
#     f1 = Field(62, 80)
#
#
# class MROAssetOutput19(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='17')
#     owner_2_id = Field(7, 26)
#     owner_2_id_qualifier = Field(27, 28)
#     owner_2_qualifier = Field(29, 29)
#     f1 = Field(30, 80)
#
#
# class MROAssetOutput20(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='18')
#     annuitant_1_name_1 = Field(7, 56)
#     f1 = Field(57, 80)
#
#
# class MROAssetOutput21(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='19')
#     annuitant_1_name_2 = Field(7, 61)
#     f1 = Field(62, 80)
#
#
# class MROAssetOutput22(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='20')
#     annuitant_1_id = Field(7, 26)
#     annuitant_1_id_qualifier = Field(27, 28)
#     annuitant_2_name_1 = Field(29, 78)
#     f1 = Field(79, 80)
#
#
# class MROAssetOutput23(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='21')
#     annuitant_2_name_2 = Field(7, 61)
#     f1 = Field(62, 80)
#
#
# class MROAssetOutput24(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='22')
#     annuitant_2_id = Field(7, 26)
#     annuitant_2_id_qualifier = Field(27, 28)
#     irs_qualification_code = Field(29, 32)
#     contract_number = Field(33, 62)
#     contract_value = Field(63, 78)
#     f1 = Field(79, 80)
#
#
# class MROAssetOutput25(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='23')
#     contract_value_as_of_date = Field(7, 14)
#     f1 = Field(15, 18)
#     delivering_associated_firm_id = Field(19, 22)
#     f2 = Field(23, 80)
#
#
# class MROAssetOutput26(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='24')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput27(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='25')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput28(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='26')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput29(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='27')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput30(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='28')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput31(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='29')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput32(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='30')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput33(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='10')
#     sedol_number_status = Field(7, 7)
#     cins_number_status = Field(8, 8)
#     delivering_firm_settlement_instruction_line_1_status = Field(9, 9)
#     delivering_firm_settlement_instruction_line_2_status = Field(10, 10)
#     delivering_firm_settlement_instruction_line_3_status = Field(11, 11)
#     delivering_firm_settlement_instruction_line_4_status = Field(12, 12)
#     delivering_firm_settlement_instruction_line_5_status = Field(13, 13)
#     f1 = Field(14, 27)
#     sedol_number = Field(28, 34)
#     cins_number = Field(35, 43)
#     delivering_firm_settlement_instruction_line_1 = Field(44, 78)
#     f2 = Field(79, 80)
#
#
# class MROAssetOutput34(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='11')
#     delivering_firm_settlement_instruction_line_2 = Field(7, 41)
#     delivering_firm_settlement_instruction_line_3 = Field(42, 76)
#     f1 = Field(77, 80)
#
#
# class MROAssetOutput35(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='12')
#     delivering_firm_settlement_instruction_line_4 = Field(7, 41)
#     delivering_firm_settlement_instruction_line_5 = Field(42, 76)
#     f1 = Field(77, 80)
#
#
# class MROAssetOutput36(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='13')
#     f1 = Field(7, 80)
#
#
# class MROAssetOutput37(BaseRecord):
#     record_type = Field(1, 1, default='M')
#     record_subtype = Field(2, 2, default='A')
#     physical_sequence_number = Field(3, 4)
#     logical_sequence_number = Field(5, 6, default='14')
#     f1 = Field(7, 80)
