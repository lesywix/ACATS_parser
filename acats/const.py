from enum import Enum


class SimpleEnum(Enum):

    @classmethod
    def keys(cls):
        # remove first under line as real key
        return [i.name if not i.name.startswith('_') else i.name.partition('_')[-1] for i in cls]

    @classmethod
    def values(cls):
        return [i.value for i in cls]

    # use key instead of Enum.name to strip '_' beginning
    @property
    def key(self):
        if self.name.startswith('_'):
            return self.name.partition('_')[-1]
        return self.name


class ACATSFileType(SimpleEnum):
    MA = 'MA'
    MT = 'MT'
    AT = 'AT'
    TI = 'TI'


class TITransactionType(SimpleEnum):
    A = 'Add'
    C = 'Change'
    R = 'Reject'
    X = 'Accelerate'


class ATTransactionType(SimpleEnum):
    A = 'Add'
    C = 'Change'
    D = 'Delete'


class TransferType(SimpleEnum):
    FRV = 'Fail Reversal'
    FUL = 'Full Transfer'
    PTD = 'Partial Transfer'
    PTF = 'Position Transfer Fund'
    PTR = 'Partial Transfer Request'
    RCL = 'Reclaim'
    RCR = 'Residual Credit'
    MFC = 'Mutual Fund Cleanup'


class OriginalReceiverCustomerAccountType(SimpleEnum):
    _4B = '403B'
    _4K = '401K'
    _5P = '529 Plan'
    _7B = '457 Plan'
    AG = 'Agency'
    BC = 'Bank Custody'
    BI = 'Beneficiary'
    BR = 'Beneficiary Roth IRA'
    CO = 'Corporate'
    CT = 'Co-Trustee'
    CU = 'Custodian'
    DR = 'Direct Rollo'
    EI = 'Coverdell IRA'
    ES = 'Estate'
    HS = 'Health Savings Account'
    IR = 'IRA'
    JT = 'Joint'
    MS = 'Medical Savings Account'
    OT = 'Other'
    QP = 'Qualified/Profit Sharing/Pension'
    RI = 'Roth IRA'
    SI = 'Simple IRA'
    SS = 'SARSEP'
    SN = 'Single'
    TR = 'Trust'


class TransferTypeReject(SimpleEnum):
    _01 = 'SS# Tax ID Mismatch'
    _02 = 'Account Title Mismatch'
    _03 = 'Documentation needed'
    _04 = 'Account Flat'
    _05 = 'Invalid Account Number'
    _06 = 'Duplicate'
    _07 = 'Account in Distribution or Transfer'
    _08 = 'Client Rescinded'
    _09 = 'Missing Authorization Signature'
    _21 = 'Account Violates Credit Policy of Receiving Firm'
    _22 = 'Unrecognized for Residual Credit Balance'
    _23 = 'Partial Transfer (Deliverer Initiated) Reject'
    _24 = 'Fail Reversal Reject'
    _25 = 'Reclaim Reject'
    _27 = 'Mutual Fund Cleanup'


class AssetCategory(SimpleEnum):
    ALT = 'Alternative Investments'
    ANNU = 'Annuity'
    CDCP = 'CD & Commercial Paper'
    CORP = 'Corporate Bond'
    EQU = 'Equities'
    FCUR = 'Foreign Currency'
    FDEB = 'Foreign Debt'
    FEQU = 'Foreign Equities'
    GOVT = 'US Govt., US Govt. Agency'
    LIFE = 'Life Insurance (Future Use only) '
    LPAR = 'Limited Partnership'
    MBS = 'FHLMC, FNMA, GNMA'
    MFMM = 'Mutual Fund-Money Market '
    MFNM = 'Mutual Fund-Non Money Market '
    MUNI = 'Municipal Bonds'
    OPT = 'Options'
    REIT = 'Real Estate Investment Trusts'
    RGT = 'Rights'
    UARP = 'Auction Rate Preferred - UIT'
    UDSC = 'Deferred Sales Charge UIT'
    UIT = 'Unit Investment Trust'
    UNT = 'Units'
    WAR = 'Warrant'
    ZERO = 'Zero Coupon Bonds'


class OptionCategory(SimpleEnum):
    _00 = 'Non option'
    _01 = 'Equity option'
    _02 = 'Non-equity option'
    _03 = 'ICS option'


class RequestedSettlingLocation(SimpleEnum):
    _00 = 'System generated settling location'
    _05 = 'CNS'
    _10 = 'Fund/SERV'
    _25 = 'DTC'
    _30 = 'Undeliverable'
    _35 = 'OCC'
    _40 = 'Cash Balance'
    _45 = 'Memo'
    _50 = 'R&D For Requested Settling Location'
    _55 = 'R&D'
    _60 = 'IPS'


class RequestedSettlingLocationReason(SimpleEnum):
    DTC = 'DTC'
    EXPO = 'Expiring Option'
    OPT = 'Option'
    USEC = 'Underlying Security'
    CRED = 'Credit Balance'
    DEB = 'Debit Balance'
    CASH = 'Underlying Cash Balance'
    COMT = 'Comment'
    SMA = 'Special Misc. Accounting Value'
    REGT = 'REG T Calls'
    _90DR = '90 Day Restriction'
    RSEC = 'Restricted Security'
    SFK = 'Safekeeping'
    XSET = 'Outside CNS, DTC, Fund/SERV, GSCC, PTC'
    FCUR = 'Foreign Currency'
    DDLE = 'Delayed Delivery'


class AssetQuantityRequestIndicator(SimpleEnum):
    F = 'Request Full Position'
    P = 'Request Partial Position'


class AssetRequestTransactionCode(SimpleEnum):
    _2 = 'Shares'
    _3 = 'Currency Amount'


class PositionCode(SimpleEnum):
    S = 'Short position'
    L = 'Long position'


class BearerBone(SimpleEnum):
    B = 'Bearer bond'
    N = 'Not bearer bond'


class CashMarginShortCode(SimpleEnum):
    C = 'Cash'
    M = 'Margin'
    S = 'Short'


class WhenIssuedIndicator(SimpleEnum):
    W = 'When issued'
    N = 'Not When issued'


class TransferTypeReason(SimpleEnum):
    _01 = 'Cash Dividend'
    _02 = 'Interest'
    _03 = 'Liquidation'
    _04 = 'Stock Dividend/Distribution'
    _05 = 'Stock Split'
    _06 = 'Reorganization'
    _07 = 'Redemption'
    _08 = 'Underlying Option'
    _09 = 'Underlying Security'
    _10 = 'Miscellaneous'
    _11 = 'Mutual Funds Fractional Cash-in-lieu'
    _12 = 'Mutual Funds Accrual '
    _13 = 'Mutual Funds Residual'
    _40 = 'Fail–position was liquidated'
    _41 = 'Fail–position in reorganization'
    _42 = 'Fail–position matured or expired'
    _43 = 'Fail–no broker/dealer agreement'
    _44 = 'Fail–fractional share quantity'
    _45 = 'Fail—non-deliverable denominations'
    _46 = 'Fail—position is non-deliverable'
    _47 = 'Fail—miscellaneous'
    _61 = 'Reclaim–duplicate delivery'
    _62 = 'Reclaim–delivered asset that did not belong to client'
    _63 = 'Reclaim–over delivery'
    _64 = 'Reclaim–fees were not withheld'
    _65 = 'Reclaim-Miscellaneous'
