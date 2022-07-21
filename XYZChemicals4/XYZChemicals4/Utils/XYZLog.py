try:
    from XYZUtil4.log import log_chemicals, LEVEL
except ImportError:
    class Null:
        def __getattr__(self, item):
            return self

        def __call__(self, *args, **kwargs):
            if len(args) == 1 and callable(args[0]):
                return args[0]
            else:
                return self

        def __getitem__(self, item):
            return self

    log_chemicals = Null()
    LEVEL = Null()
    print('\033[1;40;33m {}[{}] {} \033[0m'.format('XYZChemicals4', 'WARNING', 'PKG <XYZUtil4> is not installed!'))

log = log_chemicals.log
msg = log_chemicals.msg
