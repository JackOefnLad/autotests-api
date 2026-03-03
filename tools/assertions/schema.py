from typing import Any
from jsonschema import validate # pyright: ignore[reportMissingModuleSource]
from jsonschema.validators import Draft202012Validator # type: ignore

def validate_json_schema(instance: Any, schema:dict)->None:
    """
    Проверяет, соответсвтует ли JSON-объект заданной схеме

    :param instance: входные json-данные
    :param schema: ожидаемая json-схема 
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker = Draft202012Validator.FORMAT_CHECKER
    )

    