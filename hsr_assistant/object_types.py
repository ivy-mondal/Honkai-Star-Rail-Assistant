from hsr_assistant.data_types import Substats, RelicSets, RelicPieces, Mainstats


class Substat:   #For a single substat
    def __init__(self, substat_type: Substats, value: float):
        self.substat_type = substat_type
        self.value = value

    def display_value(self):
        if self.type.value.endswith("_"):
            return f"{self.value}%"
        return f"{self.value}"

    def __str__(self):
        return f"{self.type.value}: {self.display_value()}"

class Relic:     #For a single relic
    def __init__(self, set: RelicSets, slot: RelicPieces, rarity: int, level: int, mainstat: Mainstats, substats: list[Substat], is_equipped: str= ""):
        self.set = set
        self.slot = slot
        self.rarity = rarity
        self.level = level
        self.mainstat = mainstat
        self.substats = substats
        self.is_equipped = is_equipped

    def __str__(self):
        sub_str = "\n     ".join(str(s) for s in self.substats)
        equipped_info = f"Equipped" if self.is_equipped else "Unequipped"
        return (f"  Set:  {self.set.value}\n"
                f"  Slot:  {self.slot.value}\n"
                f"  Rarity:  {self.rarity}\n"
                f"  Level:  {self.level}\n"
                f"  Mainstat:  {self.mainstat.value}\n"
                f"  Substats:\n  {sub_str}\n"
                f"  Equipment status:  {equipped_info}\n")
