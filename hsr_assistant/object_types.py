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


class BaseCharacterStats:  # For a single maxed character without relics
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


class LightConeStats:  # For a single maxed lightcone for additional base stats only
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


class TargetBuilds:  # Target stats for each character builds
    def __init__(self, name: CharacterName, build_name=str,
                 cavern_set_name: RelicSets | None = None, planar_set_name: RelicSets | None = None,
                 body_mainstat: Mainstats | None = None, feet_mainstat: Mainstats | None = None, orb_mainstat: Mainstats | None = None, rope_mainstat: Mainstats | None = None,
                 target_substat_one: Substats | None = None, target_substat_two: Substats | None = None, target_substat_three: Substats | None = None,
                 target_substat_four: Substats | None = None, target_substat_five: Substats | None = None, target_substat_six: Substats | None = None,
                 target_stat_one_name: Mainstats | None = None, target_stat_one_value: float = 0.0,
                 target_stat_two_name: Mainstats | None = None, target_stat_two_value: float = 0.0,
                 target_stat_three_name: Mainstats | None = None, target_stat_three_value: float = 0.0,
                 target_stat_four_name: Mainstats | None = None, target_stat_four_value: float = 0.0,
                 target_stat_five_name: Mainstats | None = None, target_stat_five_value: float = 0.0,
                 target_stat_six_name: Mainstats | None = None, target_stat_six_value: float = 0.0,
                 target_stat_seven_name: Mainstats | None = None, target_stat_seven_value: float = 0.0):
        self.name = name
        self.build_name = build_name
        self.cavern_set_name = cavern_set_name
        self.planar_set_name = planar_set_name
        self.body_mainstat = body_mainstat
        self.feet_mainstat = feet_mainstat
        self.orb_mainstat = orb_mainstat
        self.rope_mainstat = rope_mainstat
        self.target_substat_one = target_substat_one
        self.target_substat_two = target_substat_two
        self.target_substat_three = target_substat_three
        self.target_substat_four = target_substat_four
        self.target_substat_five = target_substat_five
        self.target_substat_six = target_substat_six
        self.target_stat_one_name = target_stat_one_name
        self.target_stat_one_value = target_stat_one_value
        self.target_stat_two_name = target_stat_two_name
        self.target_stat_two_value = target_stat_two_value
        self.target_stat_three_name = target_stat_three_name
        self.target_stat_three_value = target_stat_three_value
        self.target_stat_four_name = target_stat_four_name
        self.target_stat_four_value = target_stat_four_value
        self.target_stat_five_name = target_stat_five_name
        self.target_stat_five_value = target_stat_five_value
        self.target_stat_six_name = target_stat_six_name
        self.target_stat_six_value = target_stat_six_value
        self.target_stat_seven_name = target_stat_seven_name
        self.target_stat_seven_value = target_stat_seven_value

    def __str__(self):
        output_string = (f"Name: {self.name.value}\n"
                         f"Build Name: {self.build_name}\n"
                         f"Cavern Set: {self.cavern_set_name.value}\n"
                         f"Planar Set: {self.planar_set_name.value}\n"
                         f"Body Mainstat: {self.body_mainstat.value}\n"
                         f"Feet Mainstat: {self.feet_mainstat.value}\n"
                         f"Orb Mainstat: {self.orb_mainstat.value}\n"
                         f"Rope Mainstat: {self.rope_mainstat}\n")

        if self.target_substat_one is not None:
            output_string += f"Substat needed: {self.target_substat_one.value}\n"

        if self.target_substat_two is not None:
            output_string += f"Substat needed: {self.target_substat_two.value}\n"

        if self.target_substat_three is not None:
            output_string += f"Substat needed: {self.target_substat_three.value}\n"

        if self.target_substat_four is not None:
            output_string += f"Substat needed: {self.target_substat_four.value}\n"

        if self.target_substat_five is not None:
            output_string += f"Substat needed: {self.target_substat_five.value}\n"

        if self.target_substat_six is not None:
            output_string += f"Substat needed: {self.target_substat_six.value}\n"

        if self.target_stat_one_name is not None:
            output_string += f"{self.target_stat_one_name.value}: {self.target_stat_one_value}\n"

        if self.target_stat_two_name is not None:
            output_string += f"{self.target_stat_two_name.value}: {self.target_stat_two_value}\n"

        if self.target_stat_three_name is not None:
            output_string += f"{self.target_stat_three_name.value}: {self.target_stat_three_value}\n"

        if self.target_stat_four_name is not None:
            output_string += f"{self.target_stat_four_name.value}: {self.target_stat_four_value}\n"

        if self.target_stat_five_name is not None:
            output_string += f"{self.target_stat_five_name.value}: {self.target_stat_five_value}\n"

        if self.target_stat_six_name is not None:
            output_string += f"{self.target_stat_six_name.value}: {self.target_stat_six_value}\n"

        if self.target_stat_seven_name is not None:
            output_string += f"{self.target_stat_seven_name.value}: {self.target_stat_seven_value}\n"

        return output_string
