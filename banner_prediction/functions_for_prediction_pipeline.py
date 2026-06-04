import json

def open_datasets(filepath):
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Where is the file bruh?!")
        return None

def make_prompt(character_data, banner_data, patch_to_predict, new_character_info, new_set_info):
    prompt_sections = []

    prompt_sections.append(f"Hello, can you predict upcoming banners in Honkai Star Rail for patch {patch_to_predict} by analyzing the past datas provided?\n")

    prompt_sections.append("Here is the comprehensive data of all existing characters in game:\n")
    for char in character_data:
        prompt_sections.append(
            f"Character: {char['name']}. Element: {char['element']}, Path: {char['path']}, "
            f"Release Patch: {char['release_patch']}, Role: {char['role']}. "
            f"Character's position in Meta at Release: {char['meta_strength_at release']}. Things to keep in mind "
            f"about this character: {char['notes']}"
        )
    prompt_sections.append("\n")

    prompt_sections.append("Here is a chronological history of all past banners since the game's release, "
                           "including rerun banners with specific reasons for their reruns:\n")
    for patch in banner_data:
        patch_info = []
        patch_info.append(f"--- Patch {patch['patch_number']} ---")
        patch_info.append(f"Notable things about the patch: {patch['notable_about_patch']}")
        patch_info.append(f"New Releases: {', '.join(patch['new_releases']) if patch['new_releases'] else 'None'}\n")

        if patch['reruns']:
            patch_info.append("Reruns:")
            for rerun in patch['reruns']:
                reason = rerun.get('probable_rerun_reason', 'No specific reason provided.')
                meta_strength = rerun.get('meta_strength_at_rerun', 'Unknown meta strength.')

                patch_info.append(
                    f"- {rerun['character_name']} ({rerun['rerun_number']}, "
                    f"{rerun['patches_since_last_appearance']} patches since last banner. "
                    f"Meta: {meta_strength}. Reason: {reason})"
                )
        else:
            patch_info.append("Reruns: (None)")
        prompt_sections.append("\n".join(patch_info))
        prompt_sections.append("\n")

    if new_character_info:
        prompt_sections.append(f"Here is the information about new releases of the patch: {new_character_info}\n")

    if new_set_info:
        prompt_sections.append(f"Here is the information about new relic set which may be relevant to reruns: "
                               f"{new_set_info}\n")

    prompt_sections.append("My general rules and observations about banner reruns are:\n")
    prompt_sections.append("- New character reruns usually happen around the 4th patch after release, unless they "
                           "have flaws in kit, then they take longer to rerun.")
    prompt_sections.append("- Consider character synergy with newly released characters or relic sets if info is "
                           "available.")
    prompt_sections.append("- Watch out for characters gaining relevance due to new game modes.\n")

    prompt_sections.append(
        f"Based on all this information, considering character attributes, historical patterns, your own pattern "
        f"analysis,"
        f"and my stated rules, please predict the most probable rerun candidates for the upcoming "
        f"**Patch {patch_to_predict}**.\n"
        f"Give a set prediction if there are 4 reruns, and another set of prediction if there are 6 reruns. "
        f"Characters can overlap in both sets."
        f"For each prediction, state the estimated probability and clearly explain why you think they will rerun, "
        f"citing specific historical patterns or reasons."
    )

    return "\n".join(prompt_sections)


character_dataset = open_datasets("character_release_history.json")
print(character_dataset)