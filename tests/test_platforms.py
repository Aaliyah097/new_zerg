from src.platforms.repo import PlatformRepo
from src.platforms.model import platform
from src.platforms.service import PlatformFabric

TEST_TOKEN = "aa244a53-c35d-4545-a3c4-35df391bdfa2"


def add():
    new_platform = PlatformFabric.get_platform(
        token=TEST_TOKEN,
        source="bitconce",
        name="USDT"
    )
    PlatformRepo.create_platform(new_platform)


def get():
    my_platform = PlatformRepo.get_platform(TEST_TOKEN)
    assert isinstance(my_platform, platform.Platform)


def get_all():
    my_platforms = PlatformRepo.get_all_platforms()
    assert type(my_platforms) == list and \
           (isinstance(my_platforms[0], platform.Platform) if len(my_platforms) != 0 else True)


def delete():
    PlatformRepo.delete_platform(TEST_TOKEN)


def update():
    my_platform = PlatformRepo.get_platform(TEST_TOKEN)
    prev_state = my_platform.is_active

    my_platform.toggle_deals()
    my_platform.name = "USDT 1"

    PlatformRepo.update_platform(my_platform)

    my_platform = PlatformRepo.get_platform(TEST_TOKEN)
    assert (my_platform.is_active != prev_state) and (my_platform.name == "USDT 1")


def test_():
    add()
    get_all()
    get()
    update()
    #delete()
    pass
