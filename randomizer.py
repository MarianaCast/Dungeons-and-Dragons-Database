#Author: Mariana Castaneda Roiz
#CS 4347.003
#Database Project: Phase 4
#This program is meant to populate the empty columns with valid entries from Dungeons and Dragons

import pandas as pd
import random
from random import randint


def main():
    weapons()
    transportation()
    armor()
    equipment()
    background()
    classes()
    player()
    race()
    spell()
    misc()

def misc():
    typeList = ["Amulet Health", "Amulet of Mighty Fists", "Bag of Holding", "Belt of Dwarfkind", "Belt of Giant Strength", "Boots of Elvenkind", "Boots of Levitation","Boots of Speed", "Bracers of Archery", "Bracers of Armor", "Chime of Opening", "Cloack of Elvenkind", "Crystal Ball", "Deck of Many Things", "Drums of Panic", "Elemental Gem", "Eversmoking Bottle", "Eyes of Petrification", "Figurines of Wondrous Power", "Gauntlet of Rust",
                "Gauntlet of Elements", "Gem of True Seeing", "Harp of Charming", "Helm of Telepathy", "Hat of Disguise", "Horn of Blasting", "Horn of Fog", "Instant Fortress", "Lantern of Revealing", "Mask of the Skull", "Mirrror of Life Trapping", "Necklace of Proof Against Poison", "Necklace of Wisdom", "Pipes of Haunting", "Portable Hole", "Robe of the Archmagi", "Rope of Entanglement", "Slippers of Spider Climbing", "Wings of Flying", "Whistle of Laughter" ]
    usageList = ["Utility", "Combat", "Damage", "Consumable", "Healing", "Container", "Combat", "Instrument", "Communication", "Exploration", "Social", "Movement", "Warding", "Deception", "Outerwear"]
    weightList = [6,8,10,13,12,20,45,20,40,40,55,60,65]

    df = pd.read_csv('misc.csv')
    type_series = df.Type.apply(lambda x: random.choice(typeList))
    df['Type'] = type_series
    usage_series = df.Usage.apply(lambda x: random.choice(usageList))
    df['Usage'] = usage_series
    weight_series = df.Weight.apply(lambda x: random.choice(weightList))
    df['Weight'] = weight_series

    df.to_csv('misc.csv')

def weapons():
    #List of all potential weapon items
    weaponsList = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", " Light Hammer", " Mace", "Quarterstaff", "Sickle", "Spear", "Crossbow", "Dart", "Shortbow", "Sling", "Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword"
                    , "Halberd", "Lance", "Longswod", "Maul", "Morningstar", "Pike", "Rapier", " Scimitar", "Shortsword","Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Crossbow - hand", "Crossbow - heavy", "Longbow", "Net"]
    rangeList = [20,60,30,120,25, 100,200,400,150,600]

    #Populate the weapons csv with all options
    df = pd.read_csv('weapons.csv')
    weapons_series = df.Type.apply(lambda x: random.choice(weaponsList))
    df['Type'] = weapons_series
    range_series = df.Range.apply(lambda x: random.choice(rangeList))
    df['Range'] = range_series

    #Write the columns into a series
    df.to_csv('weapons.csv')

def transportation():
    transportationList = ["Carriage", "Cart", "Galley", "Keelboat", "Longship", "Rowboat", "Oar", "Sailing Ship", "Sled", "Wagon", "Warship"]
    speedList = [10,20,30,40,50,60]

    df = pd.read_csv('transportation.csv')
    transport_series = df.Type.apply(lambda x: random.choice(transportationList))
    df['Type'] = transport_series
    speed_series = df.Speed.apply(lambda x: random.choice(speedList))
    df['Speed'] = speed_series

    df.to_csv('transportation.csv')

def armor():
    classList = ['Light', 'Medium', 'Heavy', 'Shield']
    typeList = ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate', 'Half Plate', 'Ring Mail', 'Chain Mail', 'Splint', 'Plate', 'Shield']
    weightList = [6,8,10,13,12,20,45,20,40,40,55,60,65]

    df = pd.read_csv('armor.csv')
    armor_series = df.Type.apply(lambda x: random.choice(typeList))
    df['Type'] = armor_series
    class_series = df.Armor_Class.apply(lambda x: random.choice(classList))
    df['Armor_Class'] = class_series
    weight_series = df.Weight.apply(lambda x: random.choice(weightList))
    df['Weight'] = weight_series

    df.to_csv('armor.csv')

def background():
    story = "To be written by player"
    jobList = ["Academic", "Adventurer", "Aporthecary", "Astronaut Trainee", "Athlete", "Blue Collar", "Celebrity", "Colonist","Creative", "Criminal","Dilettante", "Doctor", "Drifter", "Emergency Services",
                "Entrepreneur", "Gladiator", "Hedge Wizard", "Heir", "Investigative", "Law Enforcement", "Military", "Novitiate", "Outcast", "Psychic", "Religious", "Rural", "Scavenger", "Shadow Scholar", "Squire",
                "Student", "Technician", "Transporter", "White Collar"]
    characteristicsList = ["Abrasiveness", "Absent-Minded", "Aggression", "Brawler", "Cautious", "Detached", "Dishonesty", "Distinctive", "Easygoing", "Farsighted", "Focused", "Hard of hearing", "Hardy", "Honest", " Illiterate", "Inattentive", "Polite","Relentless",
                            "Slow", "Specialized", "Suspicious", "Uncivilized"] 

    df = pd.read_csv('background.csv')
    df['Story'] = story
    job_series = df.Job.apply(lambda x: random.choice(jobList))
    df['Job'] = job_series
    characteristic_series = df.Characteristics.apply(lambda x: random.choice(characteristicsList))
    df['Characteristics'] = characteristic_series

    df.to_csv('background.csv')             

def classes():
    abilityList = ["Arcana","Stealth","Religion", "Nature", "Dungeoneering", "Thievery", "Athletics", "Bluff", "Diplomacy", "Endurance", "Heal", "Insight", "Intimidate", "Streetwise"]            
    profList = ["Medium Armor","Spell Sniper", "Prodigy", "Crossbow Expert", "Dual Wielder","Sharpshooter", "Sentinel", "Lucky", "Shield Master", "Actor", "Polearm Master", "Mobile", "Alert", "War Caster", "Great Weapon Master",
                "Tough", "Resilient", "Defensive Duelist", "Observent","Elven Accuracy"]
    trainList = ["Buying a Magic Item", "Carousing", "Crafting an Item", "Crime", "Gambling", "Pit Fighting", "Relaxation", "Religious Service", "Research", "Scribing a Spell Scroll", "Selling a Magic Item", "Language", "Work", "Tool", "Stronghold", "Sowing Rumors", "Sacred Rites"]
    
    df = pd.read_csv('class.csv')

    ability_series = df.Ability.apply(lambda x: random.choice(abilityList))
    df['Ability'] = ability_series
    prof_series = df.Proficiency.apply(lambda x: random.choice(profList))
    df['Proficiency'] = prof_series
    train_series = df.Training.apply(lambda x: random.choice(trainList))
    df['Training'] = train_series

    df.to_csv('class.csv')    

def equipment():
    equipList = ['Armor', 'Weapon', 'Backpack','Treasure', 'Arrows', 'Blowgun Needles', 'Crossbow Bolts', 'Sling Bullets', 'Crystal', 'Orb', 'Rod', 'Staff', 'Wand', 'Spring Mistletoe', 'Totem', 'Wooden Staff', 'Yew Wand', 'Amulet', 'Emblem', 'Reliquary','Abacus', 'Acid', 'Alchemist Fire',
                'Antitoxin', 'Ball Bearings', 'Barrel', 'Basket', 'Bedroll', 'Bell', 'Blanket', 'Block and Tackle', 'Candle']

    df = pd.read_csv('equipment.csv')

    equip_series = df.Eq_Name.apply(lambda x: random.choice(equipList))
    df['Eq_Name'] = equip_series
    price_series = df.Price.apply(lambda x: randint(1,1000))
    df['Price'] = price_series


    df.to_csv('equipment.csv')    

def player():
    nameList = ["Mariana", "Rachel" , "Jared", "Nathan", "Renee", "Eric", "Jack", "Nick", "Cole", "Graeme", "Sabrina", "Pedro", "Dhyan", "Dhairye", "Camren", "CJ", "Andrew", "Brian" , "Kevin", "Kyle", "Ike"]

    df = pd.read_csv('player.csv')

    name_series = df.PI_Name.apply(lambda x: random.choice(nameList))
    df['PI_Name'] = name_series


    df.to_csv('player.csv')     

def race():
    sizeList = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
    languageList = ["Abyssal", "Aquan", "Auran", "Celestial", "Common", "Deep Speech", "Draconic", "Druidic", "Dravish", "Elvish", "Giant", "Gnomish", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "Primordial", "Sylvan", "Terran", "Undercommon"]
    abilityList = ["Arcana","Stealth","Religion", "Nature", "Dungeoneering", "Thievery", "Athletics", "Bluff", "Diplomacy", "Endurance", "Heal", "Insight", "Intimidate", "Streetwise"]
    traitList = ["Draenei", "Gift of the Naaru", "Heroic Presence", "Gem Cutting", "Shadow Resistence", "Explorer", "Frost Resistance", "Might of the Mountain", "Stone Form", "Arcane Resistance", "Engineering Specialist", "Escape Artist", " Expansive Mind", "Nimble Fingers",
                "Every Man for Himself", "Diplomacy", "The Human Spirit", "Elusivness", "Nature Resistence", "Quickness", " Shadow Meld", "Touch of Elune", "Wisp Spirit"]
    subList = ["Half Dragon", "Reaper Aasimar", "Winger Aasimar", "Dragon Child", "Mothra Aasimar", "Titanborn", " Zombie", "Arcadian", "Firebeard Dwarf", "Dragon Elf", "Holy Elf", "Half-Celestial", " Burly Halfling", "Elemental Born", "Fey Heritage", "Crystal Born", "Deep Dwarf", "Brae Dwarf", "Volcano Dwarf", "Urban Elf", "Sunfire Elf"]
    df = pd.read_csv('race.csv')

    ability_series = df.Abilities.apply(lambda x: random.choice(abilityList))
    df['Abilities'] = ability_series
    size_series = df.Size.apply(lambda x: random.choice(sizeList))
    df['Size'] = size_series
    language_series = df.Language.apply(lambda x: random.choice(languageList))
    df['Language'] = language_series
    trait_series = df.Traits.apply(lambda x: random.choice(traitList))
    df['Traits'] = trait_series
    sub_series = df.Sub_races.apply(lambda x: random.choice(subList))
    df['Sub_races'] = sub_series

    #del df['Ability']
    df.to_csv('race.csv')

def spell():
    spellList = ["Acid Arrow", "Acid Splash", "Aid", "Alarm", "Alter Self", "Animal Friendship", "Animal Messenger", "Animal Shape", "Animate dead", "Animate Objects", "Antlife Shell", "Antimagic Field", "Antipathy Sympathy", "Arcane Eye", "Arcane Hand", "Arcane Lock", "Arcane Sword", "Bane", "Banishment", "Beacon of Hope", "Clone", "Clairvoyance",
                    "Color Spray", "Entangle", "Enthrall", "Fireball", "Fly", "Freezing Sphere", "Gust of Wind", "Harm", "Haste", "Hideous Laughter", "Inflict Wounds", "Insect Plague", "Prismatic Wall", "Rope Trick", "Secret Chest", "Sequester"]
    componentsList = ["v s m", "v s", "v", "s", "m"]
    typeList = ["Enchantment", "Divination", "Evocation", "Illusions", "Necromancy", "Conjuration", "Transmutation", "Abjuration"]     
    rangeList = [0,30,60,90,120]    
    durationList = [1,8,24]
    castingList = [0,1,8,10]

    df = pd.read_csv('spell.csv')

    spell_series = df.Spell_Name.apply(lambda x: random.choice(spellList))
    df['Spell_Name'] = spell_series
    type_series = df.Type.apply(lambda x: random.choice(typeList))
    df['Type'] = type_series
    level_series = df.Level.apply(lambda x:randint(1,10))
    df['Level'] = level_series
    comp_series = df.Components.apply(lambda x: random.choice(componentsList))
    df['Components'] = comp_series
    range_series = df.Range.apply(lambda x: random.choice(rangeList))
    df['Range'] = range_series
    duration_series = df.Duration.apply(lambda x: random.choice(rangeList))
    df['Duration'] = duration_series
    casting_series = df.Casting_Time.apply(lambda x: random.choice(castingList))
    df['Casting_Time'] = casting_series

    df.to_csv('spell.csv')

if __name__ == "__main__":
    main()