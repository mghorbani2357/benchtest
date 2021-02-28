import time
import json
import cProfile
import pstats


class BenchMark:
    report = dict()
    functions = list()

    def __init__(self):
        self.__test()

    def __test(self):
        method_list = list()

        for function in dir(self):
            if callable(getattr(self, function)) and function.startswith('bench_test'):
                method_list.append(getattr(self, function))

        print(method_list)

        for function in method_list:
            pr = cProfile.Profile()
            pr.enable()

            function()

            pr.disable()

            ps = pstats.Stats(pr).sort_stats('tottime')
            ps.print_stats()
    #
    # def generate_report(self):
    #     print(json.dumps(self.report))

    # def bench_test(self, name, iterations=100, input_generator=None):
    #     def decorator(function):
    #         beginning_time = time.time()
    #         for i in range(iterations):
    #             function()
    #         # if name == '':
    #         name = function.__name__
    #         self.report[name] = (time.time() - beginning_time) / iterations
    #
    #     return decorator
