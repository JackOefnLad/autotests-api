from clients.users.user_schema import UserSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_equal

def assert_user(actual: UserSchema, expected: UserSchema)-> None:

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    
def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
) -> None:
    assert_user(get_user_response.user, create_user_response.user)