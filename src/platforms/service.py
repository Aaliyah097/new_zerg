from src.platforms.model import platform, bitconce_platform


class PlatformFabric:
    @staticmethod
    def get_platform(source: str, token: str, name: str) -> platform.Platform:
        if source == 'bitconce':
            my_platform = bitconce_platform.BitconcePlatform(
                token=token,
                source=source,
                name=name
            )
            return my_platform
