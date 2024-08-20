"""
Provides inbuilt int() function
"""

from funl.utils import asserter
from funl.utils import logger


def handle(params: list[str] | None) -> int:
    """
    Represents the basic int datatype

    params: list[str]   List of parameters, must be ints
    """

    if params == None or len(params) == 0:
        logger.err("INCORRECT_PARAMS", "Missing parameters for function 'uint'")
    asserter.assert_type("int", params[0], int)

    if int(params[0]) < 0:
        logger.err(
            "INCORRECT_PARAMS", "Function 'uint' cannot contain negative integers"
        )

    return int(params[0])