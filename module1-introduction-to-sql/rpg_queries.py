import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print("\nPart 1\n")


    #how many characters
print("Objective 1:")

count_characters = 'SELECT COUNT(*) FROM charactercreator_character;'
print("Total characters:", curs.execute(count_characters).fetchall())


    #How many each subclass
print("\nObjective 2:")

count_mages = 'SELECT COUNT(*) FROM charactercreator_mage;'
print("Total mages:", curs.execute(count_mages).fetchall())

count_clerics = 'SELECT COUNT(*) FROM charactercreator_cleric;'
print("Total clerics:", curs.execute(count_clerics).fetchall())

count_fighters = 'SELECT COUNT(*) FROM charactercreator_fighter;'
print("Total fighters:", curs.execute(count_fighters).fetchall())

count_necromancers = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
print("Total necromancers:", curs.execute(count_necromancers).fetchall())

count_thiefs = 'SELECT COUNT(*) FROM charactercreator_thief;'
print("Total thiefs:", curs.execute(count_thiefs).fetchall())


    #How many total items?
print("\nObjective 3:")

count_items = 'SELECT COUNT(*) FROM armory_item;'
print("Total items:", curs.execute(count_items).fetchall())


    #How many of the Items are weapons? How many are not?
print("\nObjective 4:")

count_weapons = 'SELECT COUNT() FROM armory_item JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id;'
print("Total weapons that are items:", curs.execute(count_weapons).fetchall())


#How many Items does each character have? (Return first 20 rows)
print("\nObjective 4:")
count_weapons = (f"SELECT charactercreator_character.character_id, COUNT(item_id) AS num_items "
                    f"FROM charactercreator_character "
                    f"JOIN charactercreator_character_inventory "
                    f"ON charactercreator_character_inventory.character_id = charactercreator_character.character_id "
                    f"GROUP BY charactercreator_character.character_id "
                    f"LIMIT 20")

print("- Left number is character ID, right number is amount of items. -")                   
print("How many items first 20 characters have: ", curs.execute(count_weapons).fetchall())


#On average, how many Items does each Character have?
print("\nObjective 5:")
average_items = (f"SELECT avg(count) "
                    f"FROM "
                    f"( "                
                    f"SELECT charactercreator_character.character_id, COUNT(item_id) AS count "
                    f"FROM charactercreator_character "
                    f"JOIN charactercreator_character_inventory "
                    f"ON charactercreator_character_inventory.character_id = charactercreator_character.character_id "
                    f"GROUP BY charactercreator_character.character_id "
                    f")")
print("Average items characters have: ", curs.execute(average_items).fetchall())


#On average, how many Items does each Character have?
print("\nObjective 6:")
average_weapons = (f"SELECT avg(count) "
                    f"FROM "
                    f"( "                
                    f"SELECT charactercreator_character.character_id, COUNT(item_id) AS count "
                    f"FROM charactercreator_character "
                    f"JOIN charactercreator_character_inventory "
                    f"ON charactercreator_character_inventory.character_id = charactercreator_character.character_id "
                    f"WHERE item_id BETWEEN 138 AND 174 "
                    f"GROUP BY charactercreator_character.character_id "
                    f")")
print("Average weapons characters have: ", curs.execute(average_weapons).fetchall())
