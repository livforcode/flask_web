class BaseEntity:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        """
        Converts the object to a dictionary.
        """
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_obj):
        """
        Creates an instance of the class from a dictionary.
        """
        return cls(**dict_obj)


# Example usage:


class User(BaseEntity):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id=user_id, name=name, email=email)


# Creating a User object
user = User(user_id=1, name="John Doe", email="john.doe@example.com")

# Converting User object to dictionary
user_dict = user.to_dict()
print(user_dict)

# Creating a User object from dictionary
user_from_dict = User.from_dict(user_dict)
print(user_from_dict.__dict__)
