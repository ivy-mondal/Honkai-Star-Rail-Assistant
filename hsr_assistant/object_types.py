from hsr_assistant.data_types import Substats, RelicSets, RelicPieces, Mainstats, CharacterName, Path, Element


class Substat:  # For a single substat
    def __init__(self, substat_type: Substats, value: float):
        self.substat_type = substat_type
        self.value = value

    def display_value(self):
        if self.substat_type.value.endswith("_"):
            return f"{self.value}%"
        return f"{self.value}"

    def __str__(self):
        return f"{self.substat_type.value}: {self.display_value()}"


class Relic:  # For a single relic
    def __init__(self, set: RelicSets, slot: RelicPieces, rarity: int, level: int, mainstat: Mainstats,
                 substats: list[Substat], equipped: bool = False):
        self.set = set
        self.slot = slot
        self.rarity = rarity
        self.level = level
        self.mainstat = mainstat
        self.substats = substats
        self.equipped = equipped

    def __str__(self):
        indentation = "     "

        if self.substats:
            sub_str_lines = [str(s) for s in self.substats]
            sub_str = f"\n{indentation}".join(sub_str_lines)
        else:
            sub_str = "\n     ".join(str(s) for s in self.substats)

        equipped_info = f"Equipped" if self.equipped else "Unequipped"
        return (f"  Set:  {self.set.value}\n"
                f"  Slot:  {self.slot.value}\n"
                f"  Rarity:  {self.rarity}\n"
                f"  Level:  {self.level}\n"
                f"  Mainstat:  {self.mainstat.value}\n"
                f"  Substats:\n{indentation}{sub_str}\n"
                f"  Equipment status:  {equipped_info}\n")


class BaseCharacterStats: #For a single maxed character without relics
    def __init__(self, name: CharacterName, path: Path, element: Element,
                 health: float, attack: float, defense: float, speed: float,
                 crit_rate: float, crit_damage: float,
                 break_effect: float, healing_bonus: float,
                 energy_regen_rate: float, effect_hit_rate: float,
                 effect_res: float, elation: float, damage_bonus: float):
