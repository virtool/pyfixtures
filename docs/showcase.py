from typing import Any, Protocol

from pyfixtures import fixture


def this_is_a_normal_function(a: Any, b: Any = "default_value") -> Any:
    """A regular function"""
    ...


class ReturnProtocol(Protocol):
    """A showcase return protocol"""

    def __call__(self, a: int, b: str, c: Any, d: str = "default") -> Any:
        """
        A function that does something...

        :param c: An argument to the function.

        :return: Anything, but probably nothing.
        :raises NotImplementedError: Every time.
        """


@fixture
def this_is_a_fixture(a, b, c) -> int:
    """An example fixture."""
    ...


@fixture
async def this_fixture_is_async(a: Any, b: Any = "default_value") -> Any:
    """An example async fixture"""
    ...


@fixture(hide_params=False)
def this_is_a_fixture_with_arguments(a, b="default_value") -> Any:
    """Example fixture with parameters showing"""
    ...


@fixture(protocol=ReturnProtocol)
def protocol_fixture() -> ReturnProtocol:
    ...
