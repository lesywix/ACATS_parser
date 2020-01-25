import csv

"""
use Tabule: https://github.com/tabulapdf/tabula to generate csv from PDF
then use script to generate class string and adjust manually
"""


def make_mt_class_str():
    make_class_str = ''
    count = 0
    with open('make_class_by_csv/mro_mt.csv') as f:
        r = csv.reader(f)
        for i in r:
            key = i[0]
            if key == 'Record Type':
                filler_count = 0
                count += 1
                class_name = f"\n\nclass MROTransferOutput{count:02}(BaseRecord):\n    record_type = Field({i[2]}, {i[3]}, default='M')\n"
                make_class_str += class_name
            elif key == 'FIELD NAME':
                continue
            elif key != '':
                if i[2] == '' or i[3] == '':
                    make_class_str = make_class_str.strip()
                    make_class_str, n, replace = make_class_str.rpartition('\n')

                    replace = replace.replace(' = ', f'_{key.replace(" ", "_").lower()} = ')
                    make_class_str = make_class_str + n + replace + '\n'
                    continue
                if key == 'Record Subtype':
                    make_class_str += f"    record_subtype = Field({i[2]}, {i[3]}, default='T')\n"
                    continue
                i[2], i[3] = int(i[2]), int(i[3])

                if key == 'Filler':
                    filler_count += 1
                    make_class_str += f"    f{filler_count} = Field{i[2], i[3]}\n"
                    continue
                make_class_str += f"    {i[0].replace(' ', '_').replace('/', '_or_').lower()} = Field{i[2], i[3]}\n"
    print(make_class_str)


def make_ma_class_str():
    make_class_str = ''
    count = 0
    with open('make_class_by_csv/mro_ma.csv') as f:
        r = csv.reader(f)
        for i in r:
            key = i[0]
            if key == 'Record Type':
                filler_count = 0
                count += 1
                class_name = f"\n\nclass MROAssetOutput{count:02}(BaseRecord):\n    record_type = Field({i[2]}, {i[3]}, default='M')\n"
                make_class_str += class_name
            elif key == 'FIELD NAME':
                continue
            elif key != '':
                if i[2] == '' or i[3] == '':
                    make_class_str = make_class_str.strip()
                    make_class_str, n, replace = make_class_str.rpartition('\n')

                    replace = replace.replace(' = ', f'_{key.replace(" ", "_").lower()} = ')
                    make_class_str = make_class_str + n + replace + '\n'
                    continue
                if key == 'Record Subtype':
                    make_class_str += f"    record_subtype = Field({i[2]}, {i[3]}, default='A')\n"
                    continue
                try:
                    i[2], i[3] = int(i[2]), int(i[3])
                except Exception:
                    pass

                if key == 'Filler':
                    filler_count += 1
                    make_class_str += f"    f{filler_count} = Field{i[2], i[3]}\n"
                    continue
                make_class_str += f"    {i[0].replace(' ', '_').replace('/', '_or_').lower()} = Field{i[2], i[3]}\n"
    print(make_class_str)


if __name__ == '__main__':
    # make_mt_class_str()
    make_ma_class_str()
