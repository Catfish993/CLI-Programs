# A formatter for the copy and paste job required to format content from the SRD
# Probably a lot of string manipulation and printing out to perhaps? maybe a way to automate that as well

spell_dict = {
        "spells":{
            
            }                    
        }

spell_list = [
    "Animate Dead",
    "Animate Objects",
    "Anti-Magic Shell",
    "Blade Barrier",
    "Bless",
    "Charm Animal",
    "Charm Monster",
    "Charm Person",
    "Clairvoyance",
    "Cloudkill",
    "Commune",
    "Confusion",
    "Conjure Elemental",
    "Continual Light",
    "Create Food",
    "Create Water",
    "Cure Blindness",
    "Cure Disease",
    "Cure Light Wounds",
    "Cure Serious Wounds",
    "Darkvision",
    "Death Spell",
    "Detect Evil",
    "Detect Invisible",
    "Detect Magic",
    "Dimension Door",
    "Disintegrate",
    "Dispel Evil",
    "Dispel Magic",
    "Feeblemind",
    "Find Traps",
    "Find the Path",
    "Fireball",
    "Flesh to Stone",
    "Floating Disc",
    "Fly",
    "Geas",
    "Growth of Animals",
    "Growth of Plants",
    "Hallucinatory Terrain",
    "Haste",
    "Heal",
    "Hold Monster",
    "Hold Person",
    "Hold Portal",
    "Ice Storm",
    "Insect Plague",
    "Invisibility",
    "Invisibility 10’ Radius",
    "Invisible Stalker",
    "Knock",
    "Levitate",
    "Light",
    "Lightning Bolt",
    "Locate Object",
    "Lower Water",
    "Magic Jar",
    "Magic Missile",
    "Magic Mouth",
    "Massmorph",
    "Mind Reading",
    "Mirror Image",
    "Neutralize Poison",
    "Passwall",
    "Phantasmal Force",
    "Polymorph Other",
    "Polymorph Self",
    "Projected Image",
    "Protection from Evil",
    "Protection from Evil 10’ Radius",
    "Protection from Normal Missiles",
    "Purify Food and Water",
    "Quest",
    "Raise Dead",
    "Read Languages",
    "Read Magic",
    "Regenerate",
    "Reincarnate",
    "Remove Curse",
    "Remove Fear",
    "Resist Cold",
    "Resist Fire",
    "Restoration",
    "Shield",
    "Silence 15’ Radius",
    "Sleep",
    "Speak with Animals",
    "Speak with Monsters",
    "Speak with Plants",
    "Speak with Dead",
    "Spiritual Hammer",
    "Sticks to Snakes",
    "Striking",
    "Telekinesis",
    "Teleport",
    "True Seeing",
    "Ventriloquism",
    "Wall of Fire",
    "Wall of Iron",
    "Wall of Stone",
    "Water Breathing",
    "Web",
    "Wizard Eye",
    "Wizard Lock",
    "Word of Recalla",
] 

# got the spell list. now I want to see if about formatting. Ideally I could paste in a huge amount of text and have it parse the info and format into a json file for me with the specifications that i need. 

spells_unformatted = r"""

    Clairvoyance

    Range: 60’

    Magic User 3

    Duration: 12 turns

    This spell enables the caster to see into another area through the eyes of a living creature in that area. The caster must specify the direction and approximate distance, up to a maximum of 60’ away. If there is no appropriate creature in that area, the spell fails. No saving throw is allowed, and the target creature is unaware that it is being so used. The caster may choose another subject creature after at least a turn has passed, enabling multiple locations to be viewed. If the subject creature moves out of range, contact is lost, though the caster may be able to choose another target in this case.
    Cloudkill

    Range: 100’+10’/level

    Magic User 5

    Duration: 6 rounds/level

    This spell creates a 20’x20’x20’ cloud of poison gas which moves at a rate of 10’ per round under the control of the caster (so long as he or she concentrates on it). The gas kills outright any creatures of 3 or fewer hit dice or levels it comes in contact with; creatures having 4 or more hit dice or levels must save vs. Poison or die. The cloud persists for the entire duration even if the caster ceases to concentrate upon it."""

for spell in spell_list:
    if spell in spells_unformatted:
        print(f"found {spell} in spells_unformatted")
        spell_dict["spells"][spell] = {}
        print(spell_dict)
        







