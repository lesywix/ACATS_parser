from acats.base import BaseRecord, Field


class Header(BaseRecord):
    constant_1 = Field(1, 5, default='HDR.S')
    datetrak_sysid = Field(6, 10, default='32667')
    constant_2 = Field(11, 12, default='.E')
    constant_3 = Field(13, 14, default='00')
    constant_4 = Field(15, 16, default='.C')
    originator = Field(17, 20)
    constant_5 = Field(21, 22, default='.S')
    sub_originator = Field(23, 26)
    submission_date = Field(27, 34)
    file_description = Field(35, 59, required=False)
    multi_batch_indicator = Field(60, 60, default='N')
    multi_batch_number = Field(61, 63)
    f1 = Field(64, 64, required=False)
    variable_length_record_indicator = Field(65, 65, required=False)
    f2 = Field(66, 80, required=False)


class Trailer(BaseRecord):
    constant_1 = Field(1, 5, default='END.S')
    datetrak_sysid = Field(6, 10, default='32667')
    constant_2 = Field(11, 12, default='.E')
    constant_3 = Field(13, 14, default='00')
    constant_4 = Field(15, 16, default='.C')
    originator = Field(17, 20)
    constant_5 = Field(21, 22, default='.S')
    sub_originator = Field(23, 26)
    record_count = Field(27, 33, required=False)
    f1 = Field(34, 34, required=False)
    expanded_record_count = Field(35, 43, required=False)
    f2 = Field(44, 80, required=False)
