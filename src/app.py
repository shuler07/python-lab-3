import typer
from src.factorial import factorial, factorial_recursive
from src.fibonacci import fibonacci, fibonacci_recursive
from src.sort import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)


app = typer.Typer()


@app.command("factorial", help="Calculate factorial of number")
def fact(
    n: int,
    type: str = typer.Option("iter", "--type", help="iter / recurs"),
) -> None:
    if type == "iter":
        res = factorial(n)
    else:
        res = factorial_recursive(n)

    typer.echo(res)


@app.command("fibonacci", help="Calculate fibonacci of number")
def fibo(
    n: int,
    type: str = typer.Option("iter", "--type", help="iter / recurs"),
) -> None:
    if type == "iter":
        res = fibonacci(n)
    else:
        res = fibonacci_recursive(n)

    typer.echo(res)


@app.command("sort", help="Sort list")
def sort(
    a: list[int] = typer.Argument(...),
    type: str = typer.Option(
        "quick", "--type", help="bubble / quick / counting / radix / bucket / heap"
    ),
    reverse: int = typer.Option(0, "--reverse", help="0 / 1"),
) -> None:
    reverse = reverse == 1
    match type:
        case "bubble":
            res = bubble_sort(a, reverse=reverse)
        case "quick":
            res = quick_sort(a, reverse=reverse)
        case "counting":
            res = counting_sort(a, reverse=reverse)
        case "radix":
            res = radix_sort(a, reverse=reverse)
        case "bucket":
            res = bucket_sort(a, reverse=reverse)
        case "heap":
            res = heap_sort(a, reverse=reverse)

    typer.echo(res)
