#!/bin/bash

# A CLI for easy lookup of information for the Basic Fantasy RPG
JSON_SPELLS="$HOME/Documents/Development/CLI-Programs/bfLookup/modules/SpellsData.json"

# The module the lookup starts with
module=$1
# Indicates a specific target within the chosen module.
target=$2

if [[ ! -f $JSON_SPELLS ]]; then
    echo "File not found!"
    exit 1
fi

# so if statement. if module == spells start lookup in spells and return spell name with descriptors
if [[ "$module" == "spells" ]]; then
    lookup=$(jq --arg name "$target" '.spells[] | select(.Name == $name)' "$JSON_SPELLS")
else
    echo "Target not found."
    exit 1
fi

echo "$lookup" | jq -C
