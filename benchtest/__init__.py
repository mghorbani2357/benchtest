import cProfile
import pstats

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


class BenchMark:
    report = dict()
    functions = list()
    method_list = list()
    __setup = None
    __teardown = None

    def __init__(self):
        self.__test()

    def setup(self):
        pass

    def teardown(self):
        pass

    def __test(self):
        for function in dir(self):
            if callable(getattr(self, function)) and function.startswith('test'):
                self.method_list.append(getattr(self, function))

    def bench_run(self):

        self.setup()

        for function in self.method_list:
            pr = cProfile.Profile()
            pr.enable()

            function()

            pr.disable()

            print(function.__name__ + ':')

            ps = pstats.Stats(pr).sort_stats('tottime')
            ps.print_stats()

        self.teardown()
