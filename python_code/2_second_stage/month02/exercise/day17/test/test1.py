from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
print(some_id)