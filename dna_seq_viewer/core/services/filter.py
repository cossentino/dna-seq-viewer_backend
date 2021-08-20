import pdb


class Filter():
    @classmethod
    def filter_kwargs(cls, kwargs):
        field_names = [f.name for f in cls._meta.get_fields()]
        output = {}
        for k, v in kwargs.items():
            if k in field_names:
                output[k] = v
        return output

    @classmethod
    def new(cls, *args, **kwargs):
        filtered_input = cls.filter_kwargs(kwargs)
        return cls(**filtered_input)
