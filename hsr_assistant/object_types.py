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
                 additional_stat_one_name: Mainstats | None = None,
                 additional_stat_one_value: float = 0.0,
                 additional_stat_two_name: Mainstats | None = None,
                 additional_stat_two_value: float = 0.0):
        self.name = name
        self.path = path
        self.health = health
        self.attack = attack
        self.defense = defense
        self.additional_stat_one_name = additional_stat_one_name
        self.additional_stat_one_value = additional_stat_one_value
        self.additional_stat_two_name = additional_stat_two_name
        self.additional_stat_two_value = additional_stat_two_value


    def __str__(self):
        # We start with the common parts of the string
        output_string = (f"Name: {self.name.value}\n"
                       f"Path: {self.path.value}\n"
                       f"Health: {self.health}\n"
                       f"Attack: {self.attack}\n"
                       f"Defense: {self.defense}\n")

        if self.additional_stat_one_name is not None:
            output_string += f"{self.additional_stat_one_name.value}: {self.additional_stat_one_value}\n"

        if self.additional_stat_two_name is not None:
            output_string += f"{self.additional_stat_two_name.value}: {self.additional_stat_two_value}\n"

        return output_string

# 1. Lightcone with NO additional stats
lc_no_extra = LightConeStats(
    name=LightCones.PAST_AND_FUTURE,
    path=Path.HARMONY,
    health=952,
    attack=476,
    defense=396,
    # additional_stat_one/two will default to None/0.0
)
print("--- Light Cone with NO additional stats ---")
print(lc_no_extra)
print("-" * 40)

# 2. Lightcone with ONE additional stat (Crit Damage)
lc_one_stat = LightConeStats(
    name=LightCones.CHORUS,
    path=Path.ERUDITION,
    health=1058,
    attack=582,
    defense=463,
    additional_stat_one_name=Mainstats.CRIT_DAMAGE,
    additional_stat_one_value=0.15 # 15% Crit Damage
)
print("--- Light Cone with ONE additional stat (Crit DMG) ---")
print(lc_one_stat)
print("-" * 40)

# 3. Lightcone with TWO additional stats (HP% and Speed)
lc_two_stats = LightConeStats(
    name=LightCones.MEDIATION,
    path=Path.THE_HUNT,
    health=1200,
    attack=600,
    defense=500,
    additional_stat_one_name=Mainstats.HP_PERCENT,
    additional_stat_one_value=0.12, # 12% HP
    additional_stat_two_name=Mainstats.SPEED,
    additional_stat_two_value=6 # 6 Speed
)
print("--- Light Cone with TWO additional stats (HP% and Speed) ---")
print(lc_two_stats)
print("-" * 40)
