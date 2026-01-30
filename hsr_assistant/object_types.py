from hsr_assistant.data_types import Substats, RelicSets, RelicPiece, Mainstats


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
    def __init__(self, set: RelicSets, slot: RelicPiece, rarity: int, level: int, mainstat: Mainstats, substats: list[Substats], equipped_by: str=""):
        self.set = set
        self.slot = slot
        self.rarity = rarity
        self.level = level
        self.mainstat = mainstat
        self.substats = substats
        self.equipped_by = equipped_by

    def __str__(self):
        sub_str = "\n     ".join(str(s) for s in self.substats)
        equipped_info = f"Equipped by: {self.equipped_by}" if self.equipped_by else "Unequipped"
        return (f"  Set:  {self.set.value}\n"
                f"  Slot:  {self.slot.value}\n"
                f"  Rarity:  {self.rarity}\n"
                f"  Level:  {self.level}\n"
                f"  Mainstat:  {self.mainstat.value}\n"
                f"  Substats:\n  {sub_str}\n"
                f"  Used by:  {equipped_info}\n")
