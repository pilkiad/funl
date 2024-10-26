# TODO - add module comment

from . import globalvars


def get_function_from_name(name: str, index: int = -1) -> FunctionDefinition | None:
    for environment_function in globalvars.environment[index]:
        if environment_function.name == name:
            return environment_function

    if index != len(globalvars.environment) * -1:
        return get_function_from_name(name, index=(index-1))
    else:
        return None


def get_function_index_from_name(name: str, index: int = -1) -> int | None:
    for i in range(0, len(globalvars.environment[index])):
        if globalvars.environment[i].name == name:
            return i

    if index != len(globalvars.environment) * -1:
        return get_function_from_name(name, index=(index-1))
    else:
        return None


def append_or_update(function_definition: FunctionDefinition) -> None:
    # NOTE - no possibility to change the index here since writing should only
    # be possible to the current scope
    result = get_function_index_from_name(function_definition.name)

    if result is not None:
        globalvars.environment[-1][result] = function_definition
    else:
        globalvars.environment[-1].append(function_definition)