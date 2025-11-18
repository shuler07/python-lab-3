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

    try:
        tstart = datetime.now()
        func(*args, **kwargs)
    except Exception as exc:
        raise exc

    time = datetime.now() - tstart
    return round(time.seconds + time.microseconds // 10**3) / 1000


def benchmark_sorts(
    arrays: dict[str, list], algos: dict[str, Callable]
) -> dict[str, dict[str, float]]: ...
