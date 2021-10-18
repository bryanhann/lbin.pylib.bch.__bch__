import sys
import importlib

def _fname(__file__):
    assert __file__.endswith('.py')
    path = __file__[:-3]
    for basepath in sys.path:
        basepath=basepath+'/'
        if path.startswith(basepath):
            return path[len(basepath):].replace('/','.')

def _bname(__file__):
    return '.'.join(_fname(__file__).split('.')[:3])

class ExcBCH(Exception):
    pass

class BCHCLASS:
    def _register_file(self,__file__):
        if     hasattr(self, '_file'):  raise ExcBCH( '\n\tALREADY_REGISTERED' )
        if not hasattr(self, '_file'):  self._file = __file__
        if not hasattr(self, '_fname'): self._fname = _fname(__file__)
        if not hasattr(self, '_bname'): self._bname = _bname(__file__)

    @property
    def fpath(self): return self._file

    @property
    def bname(self): return self._bname

    @property
    def fname(self): return self._fname

    def dimport(self,dotted=''):
        name = self.bname + dotted
        return importlib.import_module(name)

#
# A hack to insure only one instantiation even if this
# module is forcefully reloaded.
#

try:
    __builtins__['BCH']
except KeyError:
    __builtins__['BCH'] = BCHCLASS()

BCH=__builtins__['BCH']
