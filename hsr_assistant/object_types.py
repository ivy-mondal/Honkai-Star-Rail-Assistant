from hsr_assistant.data_types import Substats, RelicSets, RelicPieces, Mainstats, CharacterName, Path, Element, \
    LightCones


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
                 effect_res: float, elation: float, elemental_damage_bonus: float = 0.0,
                 hp_percent: float = 0.0, atk_percent: float = 0.0, def_percent: float = 0.0):
        self.name = name
        self.path = path
        self.element = element
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.break_effect = break_effect
        self.healing_bonus = healing_bonus
        self.energy_regen_rate = energy_regen_rate
        self.effect_hit_rate = effect_hit_rate
        self.effect_res = effect_res
        self.elation = elation
        self.elemental_damage_bonus = elemental_damage_bonus
        self.hp_percent = hp_percent
        self.atk_percent = atk_percent
        self.def_percent = def_percent


    def get_elemental_damage_bonus_for_element(self, query_element: Element) -> float:
        if self.element == query_element:
            return self.elemental_damage_bonus
        return 0.0

    def __str__(self):
        return (f"Name: {self.name.value}\n"
                f"Path: {self.path.value}\n"
                f"Element: {self.element.value}\n"
                f"Health: {self.health}\n"
                f"Attack: {self.attack}\n"
                f"Defense: {self.defense}\n"
                f"Speed: {self.speed}\n"
                f"Crit Rate: {self.crit_rate}%\n"
                f"Crit Damage: {self.crit_damage}%\n"
                f"Break Effect: {self.break_effect}%\n"
                f"Healing Bonus: {self.healing_bonus}%\n"
                f"Energy Regen Rate: {self.energy_regen_rate}%\n"
                f"Effect Hit Rate: {self.effect_hit_rate}%\n"
                f"Effect RES: {self.effect_res}%\n"
                f"Elation: {self.elation}\n"
                f"{self.element.value} DMG Boost: {self.elemental_damage_bonus}%\n"
                f"HP % from Traces: {self.hp_percent}%\n"
                f"ATK % from Traces: {self.atk_percent}%\n"
                f"DEF % from Traces: {self.def_percent}%\n"
                )

class LightConeStats: #For a single maxed lightcone for additional base stats only
    def __init__(self, name: LightCones, path: Path,
                 health: float, attack: float, defense: float,
                 additional_stat_name: Mainstats | None = None,
                 additional_stat_value: float = 0.0):
        self.name = name
        self.path = path
        self.health = health
        self.attack = attack
        self.defense = defense
        self.additional_stat_name = additional_stat_name
        self.additional_stat_value = additional_stat_value

    def get_additional_stat_value(self) -> float | None: # Use | None for type hinting if it can be None
        if self.additional_stat_name is not None:
            return self.additional_stat_value
        return None

    def __str__(self):
        # We start with the common parts of the string
        base_string = (f"Name: {self.name.value}\n"
                       f"Path: {self.path.value}\n"
                       f"Health: {self.health}\n"
                       f"Attack: {self.attack}\n"
                       f"Defense: {self.defense}\n")
        if self.additional_stat_name is not None:
            base_string += f"{self.additional_stat_name.value}: {self.additional_stat_value}\n"
        return base_string
