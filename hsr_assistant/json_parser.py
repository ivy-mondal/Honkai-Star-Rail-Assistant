import json
from hsr_assistant.data_types import RelicPieces, Substats, Mainstats, RelicSets
from hsr_assistant.object_types import Substat, Relic


def find_enum_member_by_value(enum_class, value_str):
    for member in enum_class:
        if member.value == value_str:
            return member
    raise ValueError(f"No member found in {enum_class.__name__} with value: {value_str}")


def parse_substat(substat_data: dict) -> Substat:
    substat_key_str = substat_data.get("key")
    substat_name = find_enum_member_by_value(Substats, substat_key_str)

    raw_value = float(substat_data.get("value"))

    return Substat(substat_type=substat_name, value=raw_value)

def parse_relic_data(json_file_path: str) -> list[Relic]:
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    relics_data = data.get("relics", [])
    parsed_relics = []

    for relic in relics_data:
        try:
            relic_set_name = relic.get("name")
            relic_set = find_enum_member_by_value(RelicSets, relic_set_name)

            relic_slot_name = relic.get("slot")
            relic_slot = find_enum_member_by_value(RelicPieces, relic_slot_name)

            relic_rarity = relic.get("rarity")
            relic_level = relic.get("level")

            main_stat_data = relic.get("mainstat")
            mainstat_name = find_enum_member_by_value(Mainstats, main_stat_data)

            sub_stat_data = relic.get("substats")
            substats = [parse_substat(s) for s in sub_stat_data if s]

            is_equipped = relic.get("location")

            parsed_relics.append(Relic(
                set=relic_set,
                slot=relic_slot,
                rarity=relic_rarity,
                level=relic_level,
                mainstat=mainstat_name,
                substats=substats,
                equipped=is_equipped != ""
            ))

        except (KeyError, ValueError) as e:
            print(f"Error parsing relic: {relics_data}. Skipping. Error: {e}")
            continue

    return parsed_relics
