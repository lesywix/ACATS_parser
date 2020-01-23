from collections import OrderedDict


class FieldValueError(ValueError):
    pass


class Field:
    def __init__(
        self,
        start: int,
        end: int,
        required: bool = True,
        default=None,
        padding=' ',
        choices=None,
        is_sequence=False,
        clean_field=None,
    ):
        self.start = start
        self.end = end
        self.required = required
        self.padding = padding
        self.default = default
        self.choices = choices
        self.is_sequence = is_sequence
        self.clean_field = clean_field

    def _validate_length(self, key, value):
        length = self.end - self.start + 1
        if len(value) > length:
            raise FieldValueError(f'length of {key}: {value} is out of range, should less than {length}')

    def _validate_choices(self, key, value):
        if value not in self.choices:
            raise FieldValueError(f'{key}: {value} is not one of {self.choices}')

    def validate(self, key, value):
        self._validate_length(key, value)
        if self.choices and self.required:
            self._validate_choices(key, value)


class RecordMeta(type):
    def __new__(cls, name, bases, attrs):
        mappings = OrderedDict()
        fields = []

        for base in bases:
            if hasattr(base, '_mappings'):
                mappings.update(base._mappings)
                fields.insert(0, base._fields)

        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                fields.append(k)

        for k in mappings.keys():
            attrs.pop(k, None)
        attrs['_mappings'] = mappings
        attrs['_fields'] = fields
        return type.__new__(cls, name, bases, attrs)


class BaseRecord(OrderedDict, metaclass=RecordMeta):
    def __init__(self, raw_string=None, *args, **kwargs):
        order_kwargs = OrderedDict()
        # create instance by raw_string if raw_string is not None
        if raw_string is not None:
            order_kwargs = self.convert_str_to_dict(raw_string)
        else:
            for key in self._mappings.keys():
                field = self._mappings[key]

                value = kwargs.get(key, field.default) or ''
                value = str(value)

                if field.clean_field and callable(field.clean_field):
                    value = field.clean_field(value)
                value = self.padding_value(key, value)

                if field.required and not value:
                    raise FieldValueError(f'key: {key} is required')

                field.validate(key, value)

                order_kwargs[key] = str(value)

        super().__init__(*args, **order_kwargs)

    def __setattr__(self, key, value):
        # convert all value to str
        value = self.padding_value(key, str(value))
        self._mappings[key].validate(key, value)
        self[key] = value

    def padding_value(self, key, value):
        field = self._mappings[key]
        field_length = field.end - field.start + 1
        if not field.required and not value:
            value = field.padding * field_length
        if value and len(value) < field_length:
            value = value + (field.padding * (field_length - len(value)))
        return value

    def get_value(self, key):
        value = getattr(self, key, None)
        return value

    def get_value_or_default(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self._mappings[key]
            if field.default is not None:
                value = field.default
                setattr(self, key, value)
        return value

    def generate_value_str(self, with_line_break=True):
        s = ''.join(self.values())
        if with_line_break:
            s += '\r\n'
        return s

    @classmethod
    def convert_str_to_dict(cls, s):
        return {k: s[field.start-1:field.end] for k, field in cls._mappings.items()}

    @classmethod
    def identify(cls, keys):
        r = ''
        for i in keys:
            r += cls._mappings[i].default
        return r


class BundleBase:
    bundle_class = None

    def __init_subclass__(cls, **kwargs):
        if not getattr(cls, 'bundle_class'):
            raise NotImplementedError('missing bundle_class class attribute')
        return super().__init_subclass__(**kwargs)

    def generate_list_of_dict(self):
        return [dict(v) for v in self.__dict__.values()]

    def generate_bundle_str(self):
        return ''.join([i.generate_value_str() for i in self.__dict__.values()])

    @classmethod
    def new_instance_from_text(cls, text: str, keys):
        """
        :param keys: list of keys for class identify
        :param text: one item of the content
        :return: Bundle instance
        """
        l = text.splitlines()
        ti_bundle = cls(
            *[c(raw_string=list(filter(lambda x: x.startswith(c.identify(keys)), l))[0]) for c in cls.bundle_class]
        )
        return ti_bundle
