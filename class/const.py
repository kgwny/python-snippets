class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()

const = _const()
const.ika = 'ika' # ok
const.hoge = 'hoge' # ok
const.hoge = 'fuga' # ng
