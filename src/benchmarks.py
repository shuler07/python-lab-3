from typing import Callable, Any
from datetime import datetime


def timeit_once(func: Callable[[Any], Any], *args: Any, **kwargs: Any) -> float:
    """
    Calculate time taken to complete a function
    Args:
        func (Callable[[Any], Any]): function to time
        *args (Any): function arguments
        **kwards (Any): function keyword-arguments
    Returns:
        float: time in seconds taken to complete a function
    Raises:
        Exception: if error occured while executing a function
    """

    tstart = datetime.now()
    func(*args, **kwargs)
    time = datetime.now() - tstart

    return round((time.seconds + time.microseconds / 10**6) * 10**5) / 10**5


def benchmark_sorts(
    arrays: dict[str, list], algos: dict[str, Callable]
) -> dict[str, dict[str, float]]:
    """
    Benchmark sorts
    Args:
        arrays (dict[str, list]): object with lists to test sortings on, key - list name, value - list
        algos (dict[str, Callable]): object with sortings to test, key - sorting name, value - sorting function
    Returns:
        dict(str, dict(str, float)): object with results, key - sorting name, value - object, where key - list name, value - taken time
    Raises:
        Exception: if error occured while executing a sorting function
    """

    results: dict[str, dict[str, float]] = {}

    for algname, algfunc in algos.items():
        results[algname] = {}
        for arrname, arrlist in arrays.items():
            results[algname][arrname] = timeit_once(algfunc, arrlist)

    return results


def print_formated_benchmark_sorts(results: dict[str, dict[str, float]]) -> None:
    "Print beatiful table with sorting functions benchmarks results"
    algos = list(results.keys())
    max_len_of_list_name = max(len(i) for i in results[list(results.keys())[0]].keys())
    print(f'|{"List name":^{max_len_of_list_name}}|', end="")
    for alg in algos:
        print(f"{alg:^16}|", end="")
    print()
    for arr in results[algos[0]].keys():
        print(f"|{arr:^{max_len_of_list_name}}|", end="")
        for alg in algos:
            res = results[alg][arr]
            print(f"{f'{res}s':^16}|", end="")
        print()
