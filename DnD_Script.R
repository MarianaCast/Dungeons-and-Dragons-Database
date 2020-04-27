library(tidyverse)
library(dplyr)
#Convert the .rda file to .csv
data <- as_tibble(DnD_Data)
#write.csv(df,"DnD_Data.csv",row.names=FALSE)

#Clean up the columns to match the database columns


#Table: Armor
# Armor_Class
# Type
# Weight
# Eq_Name_FK

#Table: Background
# BG_Name
# Story
# Job
# Characteristics

#Table: Character
# C_Name
# PI_ID_FK

#Table: Class
# Class_Name
# Ability
# HP
# Training
# Subclass 
# Proficiency

#Table: Equipment
# Eq_Name
# Price

#Table: Misc
# Usage
# Weight
# Eq_Name_FK

#Table: Player
# PI_ID
# PI_Name

#Table: Race
# Race_Name
# Size
# Language
# Abilities
# Traits
# Sub_races

#Table: Spells
# Spell_Name
# Type
# Level
# Components
# Range
# Duration
# Casting Time
# Class_Name_FK

#Table: Transportation
# Type
# Speed
# Eq_Name_Fk

#Table: Weapons
# Type
# Range
# Eq_Name_FK


#Delete columns ip, finger, hash,name, date, alignment, country, good, lawful, levelGroup
data <- subset(data, select = -c(1,2,3,4,7,14,15,16,17,18,19,20,21,27,28,29,30,31,35))

#Change the names of the columns
data <- data %>% rename(C_Name = alias, BG_Name = background, Race_Name = race, Class_Name = justClass, Level = level, Proficiency = feats, Spell_Name = spells, Casting_Time = castingStat)

data <- subset(data, select = -c(14,15,16))

#Add columns

#data$Armor_Class

data <- mutate(data,PI_ID=seq.int(nrow(data)),PI_Name = NA, Armor_Class = NA,Story = NA,Job = NA, Characteristics = NA,Ability = NA,Training = NA, Eq_Name = NA, Price = NA, Usage = NA,Size = NA, Language = NA, Abilities = NA, Traits = NA, Components = NA, Duration = NA, Speed = NA)
colnames(data)

#Export to csv
write.csv(data,"DnD_Data.csv", row.names= FALSE)
write.csv(DnD_Data,"Original_DnD_Data.csv", row.names = FALSE)