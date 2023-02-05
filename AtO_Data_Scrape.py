# =============== IMPORTS ================
import json
import os
import sys
from glob import glob
from collections import OrderedDict



# =============== CONSTANTS ================
PROJECT_PATH = "/mnt/e/Coding/Decompilation/AtO Assets Ripped/AcrossTheObelisk/ExportedProject"
OUTPUT_PATH = "/mnt/e/Coding/Decompilation/AtO Processing Output"

CARD_DATA_OUTPUT_PATH = OUTPUT_PATH + "/cardData.txt"

RESOURCES_PATH = PROJECT_PATH + "/Assets/Resources"
CARDS_PATH = RESOURCES_PATH + "/cards"
ITEMS_PATH = RESOURCES_PATH + "/items"
LOOT_PATH = RESOURCES_PATH + "/loot"
HEROES_PATH = RESOURCES_PATH + "/heroes"
SUBCLASSES_PATH = RESOURCES_PATH + "/subclass"

CARDS_WARRIOR_PATH = CARDS_PATH + "/warrior"
CARDS_MAGE_PATH = CARDS_PATH + "/mage"
CARDS_HEALER_PATH = CARDS_PATH + "/healer"
CARDS_SCOUT_PATH = CARDS_PATH + "/scout"

CARD_PATHS_TO_EXPORT = [
    CARDS_WARRIOR_PATH,
    #CARDS_MAGE_PATH,
    #CARDS_HEALER_PATH,
    #CARDS_SCOUT_PATH
]

# TODO - swap out manually entered enums with enums.json. Need humanized versions?

CARD_RARITIES = {
    0 : "Common",
    1 : "Uncommon",
    2 : "Rare",
    3 : "Epic",
    4 : "Mythic"
}

CARD_TYPES = {
    0  : "Missing card type",
    1  : "Melee attack",
    2  : "Ranged attack",
    4  : "Defense",
    5  : "Fire spell",
    6  : "Cold spell",
    7  : "Lightning spell",
    8  : "Mind spell",
    9  : "Shadow spell",
    10 : "Holy spell",
    11 : "Curse spell",
    12 : "Healing spell",
    13 : "Book",
    14 : "Small weapon",
    15 : "Song",
    16 : "Skill",
    18 : "Injury",
    #19 : castedCardType Attack?
    #20 : castedCardType Spell?
    21 : "Boon",
    22 : "Weapon",
    23 : "Armor",
    24 : "Jewelry",
    25 : "Accessory",
    26 : "Pet",
    #27 : special events? Halloween & corruption?
    28 : "Enchantment"
}

CARD_TYPES_AUX = {
    #"00000000" : "???", # TODO - what is this?
    "04000000" : "Defense",
    "05000000" : "Fire spell",
    "06000000" : "Cold spell",
    "07000000" : "Lightning spell",
    "08000000" : "Mind spell",
    "09000000" : "Shadow spell",
    "10000000" : "Skill",
    "13000000" : "Attack",
    "14000000" : "Spell"
}

CARD_CLASSES = {
    0  : "Warrior",
    1  : "Mage",
    2  : "Healer",
    3  : "Scout",
    4  : "Aura/Curse/Testing",
    5  : "Monster", # Potentially pet cards too?
    6  : "Injury",
    7  : "Boon",
    8  : "Item",
    9  : "Special", # Still unclear what this one is
    11 : "Perk"
}

TARGET_TYPES = {
    0 : "Single",
    1 : "Multiple"
}

TARGET_SIDES = {
    0 : "Monster", # TODO - does this actually mean monster, or "friendly", relative to the caster?
    1 : "Hero",
    2 : "Anyone",
    3 : "Self",
    4 : "Other Hero"
}

TARGET_POSITION = {
    0 : "", # Targetable/All
    1 : "Front",
    2 : "Random",
    3 : "Back"
    #4 : ???
    #5 : ???
    #6 : ???
    #7 : ???
    #8 : ???
    # TODO - Determine what 4-8 mean, or if they're actually used.
    #   May need to populate TARGET_STRINGS accordingly
}

TARGET_STRINGS = [
    #Single
    [
        [ "Monster",    "Front Monster", "Random Monster", "Back Monster" ],
        [ "Hero",       "Front Hero",    "Random Hero",    "Back Hero"    ],
        [ "Anyone",     "N/A",           "N/A",            "N/A"          ],
        [ "Self",       "N/A",           "N/A",            "N/A"          ],
        [ "Other Hero", "N/A",           "N/A",            "N/A"          ]
    ],
    #Multiple
    [
        [ "All Monsters", "N/A", "N/A", "N/A" ],
        [ "All Heroes",   "N/A", "N/A", "N/A" ],
        [ "Global",       "N/A", "N/A", "N/A" ],
        [ "N/A",          "N/A", "N/A", "N/A" ],
        [ "N/A",          "N/A", "N/A", "N/A" ]
    ]
]

CARD_KEYS = [ #TODO - maybe replace this with a full .asset -> object conversion, without prejudice on keys
    "cardName",
    "id",
    "upgradesTo1",
    "upgradesTo2",
    "cardUpgraded",
    "upgradedFrom",
    "baseCard",
    "description",
    "cardRarity",
    "cardType",
    "cardTypeAux",
    "cardClass",
    "energyCost",
    "autoplayDraw",
    "vanish",
    "innate",
    "targetType",
    "targetSide",
    "targetPosition",
    "ignoreBlock",
    "heal",
    "addCard",
    "addCardId",
    "addCardReducedCost"
]

TRAITS = { # Key-Value Pairs based on the .asset file keys and the string value to output
    "vanish" : "Vanish",
    "innate" : "Innate"
}


# =============== VARIABLES ================
cardsRaw = {}
cardsCollapsed = {}
cardsKeyedForFandom = {}
cardDataStr = "local data =\n{\n\t[\"Cards\"] = \n\t{\n"
progressCnt = 0
progressTotalStr = "0"


# =============== HELPER FUNCTIONS ================
# ---------- Progress Bar ----------
def updateProgressDisplay(num):
    sys.stdout.write("\rProcessing file: " + str(num) + "/" + progressTotalStr + "...")
    sys.stdout.flush()

def incrProgressDisplay():
    global progressCnt
    progressCnt += 1
    updateProgressDisplay(progressCnt)


# =============== FINDING FILES ================
# Get a list of all .asset files
# Source - https://stackoverflow.com/questions/18394147/how-to-do-a-recursive-sub-folder-search-and-return-files-in-a-list
print ("Traversing the directory for .asset files...")
card_asset_files = []
#card_asset_metafiles = []
for dir_path in CARD_PATHS_TO_EXPORT:
    card_asset_files.extend([y for x in os.walk(dir_path) for y in glob(os.path.join(x[0], '*.asset'))])
    #card_asset_metafiles.extend([y for x in os.walk(dir_path) for y in glob(os.path.join(x[0], '*.asset.meta'))])

print ("\t.asset files found: " + str(len(card_asset_files)))


# =============== PARSING DATA ================
# ---------- Pre-processing ----------
# TODO - Export any the files list as a json or something, with metadata like guid's?
#        - That way, we can break this down into steps, some of which only need to be run once per update, while iterating on other code.

print

def getValueFromCard(assetFileTxt, key):
    targetStr = "  " + key + ":"
    index = assetFileTxt.find(targetStr)
    if (index < 0):
        print("Warning: key not found in .asset file: " + key)
        return index
    indexOfNewline = assetFileTxt.find("\n", index)
    return assetFileTxt[index + len(targetStr):indexOfNewline].strip()


progressTotalStr = str(len(card_asset_files))
for file_path in card_asset_files:
    incrProgressDisplay()
    file = open(file_path, "r")
    fileTxt = file.read()
    newCard = {}
    for key in CARD_KEYS:
        value = getValueFromCard(fileTxt, key)
        if (value.isdigit()):
            newCard[key] = int(value)
        else:
            newCard[key] = value

    newCardId = newCard["id"].lower()
    cardsRaw[newCardId] = newCard
    if (newCard["cardUpgraded"] == 0):
        cardsCollapsed[newCardId] = newCard
    file.close()

print


# ---------- Export Mid-Processed JSON ----------
# TODO - Save the JSON(s) of raw card data and/or collapsed card data


# ---------- Cards ----------
def getTraits(card):
    traits = []
    for trait in TRAITS:
        if (card[trait] > 0):
            traits.append(TRAITS[trait])
    return traits

for baseCardId in cardsCollapsed:
    card = cardsCollapsed[baseCardId]
    cardA = cardsRaw[baseCardId + "a"]
    cardB = cardsRaw[baseCardId + "b"]
    cardR = cardsRaw[baseCardId + "rare"]
    cardName = card["cardName"]

    cardKeyedForFandom = OrderedDict([
        ("Name"    , cardName),
        ("Image"   , cardName + ".png"),
        ("ImageB"  , cardName + "-b.png"),
        ("ImageY"  , cardName + "-y.png"),
        ("ImageP"  , cardName + "-c.png"),
        ("Class"   , CARD_CLASSES[card["cardClass"]]),
        ("Type"    , CARD_TYPES[card["cardType"]]), # TODO - add cardTypeAux somehow too
        ("Rarity"  , CARD_RARITIES[card["cardRarity"]]),
        ("RarityB" , CARD_RARITIES[cardA["cardRarity"]]),
        ("RarityY" , CARD_RARITIES[cardB["cardRarity"]]),
        ("RarityP" , CARD_RARITIES[cardR["cardRarity"]]),
        ("Cost"    , card["energyCost"]),
        ("CostB"   , cardA["energyCost"]),
        ("CostY"   , cardB["energyCost"]),
        ("CostP"   , cardR["energyCost"]),
        ("Target"  , TARGET_STRINGS[card["targetType"]][card["targetSide"]][card["targetPosition"]]),
        ("TargetB" , TARGET_STRINGS[cardA["targetType"]][cardA["targetSide"]][cardA["targetPosition"]]),
        ("TargetY" , TARGET_STRINGS[cardB["targetType"]][cardB["targetSide"]][cardB["targetPosition"]]),
        ("TargetP" , TARGET_STRINGS[cardR["targetType"]][cardR["targetSide"]][cardR["targetPosition"]]),
        ("Text"    , card["description"]),
        ("TextB"   , cardA["description"]),
        ("TextY"   , cardB["description"]),
        ("TextP"   , cardR["description"]),
        ("Traits"  , getTraits(card)),
        ("TraitsB" , getTraits(cardA)),
        ("TraitsY" , getTraits(cardB)),
        ("TraitsP" , getTraits(cardR))
    ])

    cardsKeyedForFandom[baseCardId] = cardKeyedForFandom

for cardId in cardsKeyedForFandom:
    card = cardsKeyedForFandom[cardId]
    cardDataStr += "\t\t{\n"
    for key, value in card.items():
        # TODO - only add quotes here if it's a string?
        cardDataStr += "\t\t\t" + key + " = " + json.dumps(value) + ",\n"
    cardDataStr += "\t\t},\n"


# TODO - Interpret the description text and substitute values like "<AddCard><Card>" and "<AddCardType>"
#   description: '<Discover> <AddCard><Card> <AddCardType> and shuffle them into your deck with <sy>cost 0</sy> and <sy>vanish.</sy>'


# ---------- Locations & Events ----------
# TODO - Locations = world/mapnodes/...
#        - nodeEvent = list of (possible?) events. guid points to meta file for event asset:
#      - Events = world/events/...
#        - ssLootList = loot list for what condition(s)? guid points to meta file for loot asset:
#      - Loot lists = loot/...
#        - lootItemTable = list of lootCards. guid points to meta file for... item, maybe other stuff? Cards?


# ---------- Items ----------
# TODO - Items


# ---------- Classes & Subclasses ----------
# TODO - Classes & Subclasses


# =============== FINAL CLEANUP & EXPORT ================
cardDataStr += "\t}\n}\nreturn data"

#print ("\nFinal output:")
#print (cardDataStr)

print ("Writing to " + CARD_DATA_OUTPUT_PATH)
file = open(CARD_DATA_OUTPUT_PATH, "w")
file.write(cardDataStr)
file.close()
print ("  Done writing")
