from hsr_assistant.json_parser import parse_relic_data

if __name__ == "__main__":
    json_path = "sample_file.json"

    print(f"Attempting to parse relics from: {json_path}\n")
    relics = parse_relic_data(json_path)

    if relics:
        print(f"Successfully parsed {len(relics)} relics!")
        print("\n--- First 50 Parsed Relics ---")
        for i, relic in enumerate(relics[:50]):
            print(f"\n{relic}")
    else:
        print("No relics parsed or an error occurred during parsing.")