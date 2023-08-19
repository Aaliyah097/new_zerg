from src.users.repo import UserRepo
from src.users.model import user

TEST_TELEGRAM = "@thedawnofmydeath"


def add():
    new_user = user.User(
        telegram=TEST_TELEGRAM
    )

    UserRepo.create_user(new_user)


def get():
    my_user = UserRepo.get_user(TEST_TELEGRAM)
    assert isinstance(my_user, user.User)


def update():
    my_user = UserRepo.get_user(TEST_TELEGRAM)
    prev_state = my_user.is_active

    my_user.toggle_active()
    UserRepo.update_user(my_user)

    my_user = UserRepo.get_user(TEST_TELEGRAM)

    assert my_user.is_active != prev_state


def get_all():
    users = UserRepo.get_all_users()
    assert type(users) == list and \
           (isinstance(users[0], user.User) if len(users) != 0 else True)


def delete():
    UserRepo.delete_user(TEST_TELEGRAM)

    assert not UserRepo.get_user(TEST_TELEGRAM)


def test_():
    add()
    get()
    update()
    get_all()
    #delete()
    pass
