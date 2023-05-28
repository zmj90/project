import yaml


class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp

    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)


o = yaml.load("""
!!python/object:__main__.Hero
name: Welthyr Syxgon
hp: 1200
sp: 0
""",
              # yaml.BaseLoader)
              # yaml.FullLoader)
              # yaml.SafeLoader)
yaml.Loader)
# yaml.UnsafeLoader)
print(o)
