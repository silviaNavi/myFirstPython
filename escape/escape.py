# Escape - A python Adventure
#  Main fraim by Sean McManus
#  customized by Silvia Navalesi

import time, random, math


############
# VARIABLES##
############

WIDTH=800
HEIGHT=800

TILE_SIZE=30


player_y,player_x= 2,5
game_over= False

PLAYER ={
    "left" :[images.spacesuit_left, images.spacesuit_left_1,
             images.spacesuit_left_2,images.spacesuit_left_3,
             images.spacesuit_left_4
             ],
    "right" :[images.spacesuit_right, images.spacesuit_right_1,
             images.spacesuit_right_2,images.spacesuit_right_3,
             images.spacesuit_right_4
             ],
    "up" :[images.spacesuit_back, images.spacesuit_back_1,
             images.spacesuit_back_2,images.spacesuit_back_3,
             images.spacesuit_back_4
             ],
    "down" :[images.spacesuit_front, images.spacesuit_front_1,
             images.spacesuit_front_2,images.spacesuit_front_3,
             images.spacesuit_front_4
             ]
    
    }
PLAYER_SHADOW ={
    "left" :[images.spacesuit_left_shadow, images.spacesuit_left_1_shadow,
             images.spacesuit_left_2_shadow,images.spacesuit_left_3_shadow,
             images.spacesuit_left_4_shadow
             ],
    "right" :[images.spacesuit_right_shadow, images.spacesuit_right_1_shadow,
             images.spacesuit_right_2_shadow,images.spacesuit_right_3_shadow,
             images.spacesuit_right_4_shadow
             ],
    "up" :[images.spacesuit_back_shadow, images.spacesuit_back_1_shadow,
             images.spacesuit_back_2_shadow,images.spacesuit_back_3_shadow,
             images.spacesuit_back_4_shadow
             ],
    "down" :[images.spacesuit_front_shadow, images.spacesuit_front_1_shadow,
             images.spacesuit_front_2_shadow,images.spacesuit_front_3_shadow,
             images.spacesuit_front_4_shadow
             ]
    
    }

player_direction = "down"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_image_shadow = PLAYER_SHADOW[player_direction][player_frame]
player_offset_x,player_offset_y=0,0



#PILLARS
PILLARS=[images.pillar,images.pillar_95,images.pillar_80,images.pillar_60,images.pillar_50]
wall_transparency_frame=0
BLACK =(0,0,0)
BLUE=(0,155,155)
YELLOW=(255,255,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(128,0,0)

#GAME VARIABLES
air, energy =100,100
suit_stiched, air_fixed = False,False
launch_frame = 0

#PLAYER variables
PLAYER_NAME= "Silvia"
FRIEND1_NAME= "Marcella"
FRIEND2_NAME= "Nicola"
current_room= 31

top_left_x=100
top_left_y=150

#DEMO_OBJECTS= [images.floor, images.pillar, images.soil]

LANDER_SECTOR =random.randint(1,24)
LANDER_X = random.randint(2,11)
LANDER_Y =  random.randint(2,11)

objects = {
    0: [images.floor, None, "The floor is shiny and clean"],
    1: [images.pillar, images.full_shadow, "The wall is smooth and cold"],
    2: [images.soil, None, "It's like a desert. Or should that be dessert?"],
    3: [images.pillar_low, images.half_shadow, "The wall is smooth and cold"],
    4: [images.bed, images.half_shadow, "A tidy and comfortable bed"],
    5: [images.table, images.half_shadow, "It's made from strong plastic."],
    6: [images.chair_left, None, "A chair with a soft cushion"],
    7: [images.chair_right, None, "A chair with a soft cushion"],
    8: [images.bookcase_tall, images.full_shadow,
        "Bookshelves, stacked with reference books"],
    9: [images.bookcase_small, images.half_shadow,
        "Bookshelves, stacked with reference books"],
    10: [images.cabinet, images.half_shadow,
         "A small locker, for storing personal items"],
    11: [images.desk_computer, images.half_shadow,
         "A computer. Use it to run life support diagnostics"],
    12: [images.plant, images.plant_shadow, "A spaceberry plant, grown here"],
    13: [images.electrical1, images.half_shadow,
         "Electrical systems used for powering the space station"],
    14: [images.electrical2, images.half_shadow,
         "Electrical systems used for powering the space station"],
    15: [images.cactus, images.cactus_shadow, "Ouch! Careful on the cactus!"],
    16: [images.shrub, images.shrub_shadow,
         "A space lettuce. A bit limp, but amazing it's growing here!"],
    17: [images.pipes1, images.pipes1_shadow, "Water purification pipes"],
    18: [images.pipes2, images.pipes2_shadow,
         "Pipes for the life support systems"],
    19: [images.pipes3, images.pipes3_shadow,
         "Pipes for the life support systems"],
    20: [images.door, images.door_shadow, "Safety door. Opens automatically \
for astronauts in functioning spacesuits."],
    21: [images.door, images.door_shadow, "The airlock door. \
For safety reasons, it requires two person operation."],
    22: [images.door, images.door_shadow, "A locked door. It needs " \
         + PLAYER_NAME + "'s access card"],
    23: [images.door, images.door_shadow, "A locked door. It needs " \
         + FRIEND1_NAME + "'s access card"],
    24: [images.door, images.door_shadow, "A locked door. It needs " \
         + FRIEND2_NAME + "'s access card"],
    25: [images.door, images.door_shadow,
         "A locked door. It is opened from Main Mission Control"],
    26: [images.door, images.door_shadow,
         "A locked door in the engineering bay."],
    27: [images.map, images.full_shadow,
         "The screen says the crash site was Sector: " \
         + str(LANDER_SECTOR) + " // X: " + str(LANDER_X) + \
         " // Y: " + str(LANDER_Y)],
    28: [images.rock_large, images.rock_large_shadow,
         "A rock. Its coarse surface feels like a whetstone", "the rock"],
    29: [images.rock_small, images.rock_small_shadow,
         "A small but heavy piece of Martian rock"],
    30: [images.crater, None, "A crater in the planet surface"],
    31: [images.fence, None,
         "A fine gauze fence. It helps protect the station from dust storms"],
    32: [images.contraption, images.contraption_shadow,
         "One of the scientific experiments. It gently vibrates"],
    33: [images.robot_arm, images.robot_arm_shadow,
         "A robot arm, used for heavy lifting"],
    34: [images.toilet, images.half_shadow, "A sparkling clean toilet"],
    35: [images.sink, None, "A sink with running water", "the taps"],
    36: [images.globe, images.globe_shadow,
         "A giant globe of the planet. It gently glows from inside"],
    37: [images.science_lab_table, None,
         "A table of experiments, analyzing the planet soil and dust"],
    38: [images.vending_machine, images.full_shadow,
         "A vending machine. It requires a credit.", "the vending machine"],
    39: [images.floor_pad, None,
         "A pressure sensor to make sure nobody goes out alone."],
    40: [images.rescue_ship, images.rescue_ship_shadow, "A rescue ship!"],
    41: [images.mission_control_desk, images.mission_control_desk_shadow, \
         "Mission Control stations."],
    42: [images.button, images.button_shadow,
         "The button for opening the time-locked door in engineering."],
    43: [images.whiteboard, images.full_shadow,
         "The whiteboard is used in brainstorms and planning meetings."],
    44: [images.window, images.full_shadow,
         "The window provides a view out onto the planet surface."],
    45: [images.robot, images.robot_shadow, "A cleaning robot, turned off."],
    46: [images.robot2, images.robot2_shadow,
         "A planet surface exploration robot, awaiting set-up."],
    47: [images.rocket, images.rocket_shadow, "A one-person craft in repair"], 
    48: [images.toxic_floor, None, "Toxic floor - do not walk on!"],
    49: [images.drone, None, "A delivery drone"],
    50: [images.energy_ball, None, "An energy ball - dangerous!"],
    51: [images.energy_ball2, None, "An energy ball - dangerous!"],
    52: [images.computer, images.computer_shadow,
         "A computer workstation, for managing space station systems."],
    53: [images.clipboard, None,
         "A clipboard. Someone has doodled on it.", "the clipboard"],
    54: [images.bubble_gum, None,
         "A piece of sticky bubble gum. Spaceberry flavour.", "bubble gum"],
    55: [images.yoyo, None, "A toy made of fine, strong string and plastic. \
Used for antigrav experiments.", PLAYER_NAME + "'s yoyo"],
    56: [images.thread, None,
         "A piece of fine, strong string", "a piece of string"],
    57: [images.needle, None,
         "A sharp needle from a cactus plant", "a cactus needle"],
    58: [images.threaded_needle, None,
         "A cactus needle, spearing a length of string", "needle and string"],
    59: [images.canister, None,
         "The air canister has a leak.", "a leaky air canister"],
    60: [images.canister, None,
         "It looks like the seal will hold!", "a sealed air canister"],
    61: [images.mirror, None,
         "The mirror throws a circle of light on the walls.", "a mirror"], 
    62: [images.bin_empty, None,
         "A rarely used bin, made of light plastic", "a bin"],
    63: [images.bin_full, None,
         "A heavy bin full of water", "a bin full of water"],
    64: [images.rags, None,
         "An oily rag. Pick it up by one corner if you must!", "an oily rag"], 
    65: [images.hammer, None,
         "A hammer. Maybe good for cracking things open...", "a hammer"],
    66: [images.spoon, None, "A large serving spoon", "a spoon"],
    67: [images.food_pouch, None,
         "A dehydrated food pouch. It needs water.", "a dry food pack"], 
    68: [images.food, None,
         "A food pouch. Use it to get 100% energy.", "ready-to-eat food"], 
    69: [images.book, None, "The book has the words 'Don't Panic' on the \
cover in large, friendly letters", "a book"], 
    70: [images.mp3_player, None,
         "An MP3 player, with all the latest tunes", "an MP3 player"],
    71: [images.lander, None, "The Poodle, a small space exploration craft. \
Its black box has a radio sealed inside.", "the Poodle lander"],
    72: [images.radio, None, "A radio communications system, from the \
Poodle", "a communications radio"],
    73: [images.gps_module, None, "A GPS Module", "a GPS module"],
    74: [images.positioning_system, None, "Part of a positioning system. \
Needs a GPS module.", "a positioning interface"],
    75: [images.positioning_system, None,
         "A working positioning system", "a positioning computer"],
    76: [images.scissors, None, "Scissors. They're too blunt to cut \
anything. Can you sharpen them?", "blunt scissors"],
    77: [images.scissors, None,
         "Razor-sharp scissors. Careful!", "sharpened scissors"],
    78: [images.credit, None,
         "A small coin for the station's vending systems",
         "a station credit"],
    79: [images.access_card, None,
         "This access card belongs to " + PLAYER_NAME, "an access card"],
    80: [images.access_card, None,
         "This access card belongs to " + FRIEND1_NAME, "an access card"],
    81: [images.access_card, None,
         "This access card belongs to " + FRIEND2_NAME, "an access card"]
    }

items_player_may_carry = list(range(53, 82))
# Numbers below are for floor, pressure pad, soil, toxic floor.
items_player_may_stand_on = items_player_may_carry + [0, 39, 2, 48]

###############
##  SCENERY  ##
###############   <key=room Numbe>: <objectNumber>, <object_y_coordinate>, <object_x_coordinate>

# Scenery describes objects that cannot move between rooms.
# room number: [[object number, y position, x position], [...]...]
scenery = {
    26: [[39,8,2,],],
    27: [[33,5,5], [33,1,1], [33,1,8], [47,5,2],
         [47,3,10], [47,9,8], [42,1,6]],
    28: [[27,0,3], [41,4,3], [41,4,7]],
    29: [[7,2,6], [6,2,8], [12,1,13], [44,0,1],
         [36,4,10], [10,1,1], [19,4,2], [17,4,4]],
    30: [[34,1,1], [35,1,3]],
    31: [[11,1,1], [19,1,8], [46,1,3]],
    32: [[48,2,2], [48,2,3], [48,2,4], [48,3,2], [48,3,3],
         [48,3,4], [48,4,2], [48,4,3], [48,4,4]],
    33: [[13,1,1], [13,1,3], [13,1,8], [13,1,10], [48,2,1],
         [48,2,7], [48,3,6], [48,3,3]],
    34: [[37,2,2], [32,6,7], [37,10,4], [28,5,3]],
    35: [[16,2,9], [16,2,2], [16,3,3], [16,3,8], [16,8,9], [16,8,2], [16,1,8],
         [16,1,3], [12,8,6], [12,9,4], [12,9,8],
         [15,4,6], [12,7,1], [12,7,11]],
    36: [[4,3,1], [9,1,7], [8,1,8], [8,1,9],
         [5,5,4], [6,5,7], [10,1,1], [12,1,2]],
    37: [[48,3,1], [48,3,2], [48,7,1], [48,5,2], [48,5,3],
         [48,7,2], [48,9,2], [48,9,3], [48,11,1], [48,11,2]],
    38: [[43,0,2], [6,2,2], [6,3,5], [6,4,7], [6,2,9], [45,1,10]],
    39: [[38,1,1], [7,3,4], [7,6,4], [5,3,6], [5,6,6],
         [6,3,9], [6,6,9], [45,1,11], [12,1,8], [12,1,4]], 
    40: [[41,5,3], [41,5,7], [41,9,3], [41,9,7],
         [13,1,1], [13,1,3], [42,1,12]],
    41: [[4,3,1], [10,3,5], [4,5,1], [10,5,5], [4,7,1],
         [10,7,5], [12,1,1], [12,1,5]],
    42: [[42,0,2]],
    43: [[52,4,3],[42,0,2]],
    44: [[46,4,3], [46,4,5], [18,1,1], [19,1,3],
         [19,1,5], [52,4,7], [14,1,8]],
    45: [[48,2,1], [48,2,2], [48,3,3], [48,3,4], [48,1,4], [48,1,1]],
    46: [[10,1,1], [4,1,2], [8,1,7], [9,1,8], [8,1,9], [5,4,3], [7,3,2]],
    47: [[9,1,1], [9,1,2], [10,1,3], [12,1,7], [5,4,4], [6,4,7], [4,1,8]],
    48: [[17,4,1], [17,4,2], [17,4,3], [17,4,4], [17,4,5], [17,4,6], [17,4,7],
         [17,8,1], [17,8,2], [17,8,3], [17,8,4],
         [17,8,5], [17,8,6], [17,8,7], [14,1,1]],
    49: [[14,2,2], [14,2,4], [7,5,1], [5,5,3], [48,3,3], [48,3,4]], 
    50: [[45,4,8], [11,1,1], [13,1,8], [33,2,1], [46,4,6]] 
    }

checksum = 0
check_counter = 0
for key, room_scenery_list in scenery.items():
    for scenery_item_list in room_scenery_list:
        checksum += (scenery_item_list[0] * key
                     + scenery_item_list[1] * (key + 1) 
                     + scenery_item_list[2] * (key + 2))
        check_counter += 1
print(check_counter, "scenery items")
assert check_counter == 164, "Expected for scenery items"
print(checksum, "checksum")
assert checksum == 206390, "Error in scenery data"
print("Scenery checksum: " + str(checksum))


###adding objects randomly to internal room
### adding fence to the outside space

for room in range(1,26):
     if room != 13:
          scenery_item =random.choice([16,28,29,30])
          scenery[room] = [[scenery_item, random.randint(2,10),
                            random.randint(2,10)]]

for room_coordinate in  range(0,13):
     for room_number in [1,2,3,4,5]:
          scenery[room_number] += [[31,0,room_coordinate]]
     for room_number in [1,6,11,16,21]:
          scenery[room_number] += [[31,room_coordinate,0]]
     for room_number in [5,10,15,20,25]:
          scenery[room_number] += [[31,room_coordinate,12]]

del scenery[21][-1]
del scenery[25][-1]



          

###

#####
# MAP#
########

MAP_WIDTH= 5
MAP_HEIGHT=10
MAP_SIZE= MAP_WIDTH * MAP_HEIGHT

#######
#   game_map = [["Room Name", <height>, <width>, <hasExitTop>, <hasExitRight>],[..]
#####
GAME_MAP= [[ "Room 0 - where unused objects are kept",0 ,0, False, False]]

outdoor_rooms = range(1,26)
for planetsectors in range(1,26):
     GAME_MAP.append(["The dusty planet surface", 13,13, True, True])


GAME_MAP += [["The airlock",13,5,True,False], #room 26
             ["The  engineering lab",13,13,False,False], # room 27
             ["Poodle Mission Control",9,13,False,True],#28
             ["The viewing gallery",9,15,False,False], #29
             ["The crew's bathroom",5,5,False,False], #30
             ["The airlock entry bay",7,11,True,True], #room 31
             ["Left elbow room",9,7,True,False], #32
             ["Right elbow room",7,13,True,True], #33             
             ["The Science lab",13,13,False, True],#34
             ["The Greenhouse",13,13,True,False], #35
             [PLAYER_NAME + "'s sleeping quarters",9,11,False,False], #36
             
             ["West Corridor",15,5,True,True], #room 37
             
             ["The Briefing room",7,13,False,True],#38
             ["The crew's community room",11,13,True,True],#39
             ["Main Mission Control",14,14,False,False],#40
             ["Sick bay",12,7,True,False],#41
             ["Est Corridor",9,7,True,False],#42
             ["Utilities control room",9,9,False,True], #43
             ["System Engineering bay",9,11,False,False],
             ["Security portal to Mission Control",7,7,True,False],
             [FRIEND1_NAME +"'s Sleeping quarters",9,11,True,True],
             [FRIEND2_NAME +"'s Sleeping quarters",9,11,True,True],
             ["The pipeworks",13,11,True,False],
             ["The chief scientist's office",9,7,True,True],
             ["The robot workshop",9,11,True,False]]

 #sanity check
assert len(GAME_MAP)-1 == MAP_SIZE, "Map size  and GAME_MAP don't match"



def get_floor_type():
    if current_room in outdoor_rooms:
        return 2
    else:
        return 0

def generate_map():
#function to create the map for the current room.
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type()
    if current_room in range(1,21):
        bottom_edge =2 #soil
        side_edge =2 #soli
    if current_room in range(21,26):
        bottom_edge = 1 #wall
        side_edge =  2 #soil
    if current_room > 25:
        bottom_edge = 1 #wall
        side_edge =  1 #wall


#create a top line of room map

#top
    room_map = [[side_edge] * room_width] 
#middle
    for y in range( room_height - 2):
        room_map.append([side_edge] +[floor_type]* (room_width - 2) + [side_edge])
#bottom
    room_map.append([bottom_edge]* room_width)

#doorways
    middle_row = int(room_height/2)
    middle_column = int(room_width/2)


    if room_data[4]: #== true there is an exiton the right
        room_map[middle_row][room_width -1] = floor_type
        room_map[middle_row+1][room_width -1 ] = floor_type
        room_map[middle_row-1][room_width-1] = floor_type

    if current_room % MAP_WIDTH != 1: #if room is not on the left of map
        room_to_left = GAME_MAP[current_room -1]
    #if room on the left has a right exit,add left exit in this room
        if room_to_left[4]:
            room_map [middle_row][0] = floor_type
            room_map [middle_row +1][0] = floor_type
            room_map [middle_row -1][0] = floor_type

    if room_data[3]: # if exit on the top
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column + 1] = floor_type
        room_map[0][middle_column - 1] = floor_type


    if current_room <= MAP_SIZE - MAP_WIDTH:  #not at the bottom row
       room_below= GAME_MAP[current_room+MAP_WIDTH]
       # add exist top and bottom if they exists
       if room_below[3]:
           room_map[room_height-1][middle_column] = floor_type
           room_map[room_height-1][middle_column + 1] = floor_type
           room_map[room_height-1][middle_column - 1] = floor_type


#adding forniture or scenery
           
    if  current_room in scenery:
         for this_scenery in scenery[current_room]:
              scenery_number = this_scenery[0]
              scenery_y = this_scenery[1]
              scenery_x = this_scenery[2]

              room_map[scenery_y][scenery_x] = scenery_number
              image_here=objects[scenery_number][0]
              image_width=image_here.get_width()
              image_width_in_tiles=int(image_width/TILE_SIZE)

              for tile_number in range(1, image_width_in_tiles):
                   room_map[scenery_y][scenery_x + tile_number] = 255
                   
    center_y= int(HEIGHT/2)
    center_x= int(WIDTH/2)
    room_pixel_width = room_width * TILE_SIZE
    room_pixel_height = room_height * TILE_SIZE
    top_left_x= center_x -0.5* room_pixel_width
    top_left_y = (center_y-0.5 * room_pixel_height)+110

    ### adding props - object the player can pick up
    for prop_number, prop_info in props.items():
        prop_room= prop_info[0]
        prop_y=prop_info[1]
        prop_x=prop_info[2]
        if (prop_room == current_room and room_map[prop_y][prop_x] in [0,39,2]):
                room_map[prop_y][prop_x] = prop_number
                image_here = objects[prop_number][0]
                image_width = image_here.get_width()
                image_width_in_tiles = int(image_width/TILE_SIZE)
                for tile_number in range(1,image_width_in_tiles):
                    room_map[prop_y][prop_x+tile_number] =255

    hazard_map =[]
    for y in range(room_height):
        hazard_map.append([0]* room_width)

        
###############
## GAME LOOP ##
###############
def start_room():
    global airlock_door_frame
    show_text("You are  here: " + room_name,0)
    if current_room == 26: #door with the airlock
        airlock_door_frame=0
        clock.schedule_interval(door_in_room_26,0.05)
    hazard_start()
                
def game_loop():
    global player_x, player_y, current_room
    global from_player_x, from_player_y
    global player_image, player_image_shadow 
    global selected_item, item_carrying, energy 
    global player_offset_x, player_offset_y
    global player_frame, player_direction

    if game_over:
        return
###is the player walking ? it needs to move for 4 frames to complete a move
    if player_frame > 0:  
        player_frame += 1
        time.sleep(0.05) 
        if player_frame == 5:
            player_frame = 0
            player_offset_x = 0
            player_offset_y = 0

# save player's current position
    old_player_x = player_x
    old_player_y = player_y

# move if key is pressed
    if player_frame == 0:
        if keyboard.right:
            from_player_x = player_x
            from_player_y = player_y
            player_x += 1
            player_direction = "right"
            player_frame = 1
        elif keyboard.left: #elif stops player making diagonal movements
            from_player_x = player_x
            from_player_y = player_y
            player_x -= 1
            player_direction = "left"
            player_frame = 1
        elif keyboard.up:
            from_player_x = player_x
            from_player_y = player_y
            player_y -= 1
            player_direction = "up"
            player_frame = 1
        elif keyboard.down:
            from_player_x = player_x
            from_player_y = player_y
            player_y += 1
            player_direction = "down"
            player_frame = 1

# check for exiting the room
# through door on RIGHT
    if player_x == room_width: 
        clock.unschedule(hazard_move)
        current_room += 1
        generate_map()
        player_x = 0 # enter at left
        player_y = int(room_height / 2) # enter at door
        player_frame = 0
        start_room()
        return

    # through door on LEFT

    if player_x == -1: 
        clock.unschedule(hazard_move)
        current_room -= 1
        generate_map()
        player_x = room_width - 1  # enter at right
        player_y = int(room_height / 2) # enter at door
        player_frame = 0
        start_room()
        return
# through door at BOTTOM
    if player_y == room_height: 
        clock.unschedule(hazard_move)
        current_room += MAP_WIDTH
        generate_map()
        player_y = 0 # enter at top
        player_x = int(room_width / 2) # enter at door
        player_frame = 0
        start_room()
        return


# through door at TOP
    if player_y == -1: 
        clock.unschedule(hazard_move)
        current_room -= MAP_WIDTH
        generate_map()
        player_y = room_height - 1 # enter at bottom
        player_x = int(room_width / 2) # enter at door
        player_frame = 0
        start_room()
        return
    if keyboard.g:
        pick_up_object()

    if keyboard.tab and len(in_my_pockets) >0:
        selected_item +=1
        if selected_item > len(in_my_pockets) -1:
            selected_item =0
        item_carrying = in_my_pockets[selected_item]
        display_inventory()
        
    if keyboard.d and item_carrying:
        drop_object(old_player_y, old_player_x)
        
    if keyboard.space:
        examine_object()
    
    if keyboard.u:
        use_object()
        #teleport
#    if keyboard.k:
#        current_room = int(input("Enter room number:"))
#        player_x, player_y =2,2
#        generate_map()
#        start_room()
#        sounds.teleport.play()
        

  # If the player is standing somewhere they shouldn't, move them back.
    if room_map[player_y][player_x] not in items_player_may_stand_on  or hazard_map[player_y][player_x] != 0:
        player_x = old_player_x
        player_y = old_player_y
        player_frame = 0

    if room_map[player_y][player_x] == 48: # toxic floor
        deplete_energy(1)
        print( "Danger ")

    if player_direction == "right" and player_frame > 0:
        player_offset_x = -1 + (0.25 * player_frame)
    if player_direction == "left" and player_frame > 0:
        player_offset_x = 1 - (0.25 * player_frame)
    if player_direction == "up" and player_frame > 0:
        player_offset_y = 1 - (0.25 * player_frame)
    if player_direction == "down" and player_frame > 0:
        player_offset_y = -1 + (0.25 * player_frame)

###########
##  DISPLAY ###
################


def draw_image(image,y,x):
    screen.blit(
        image,
        (top_left_x + (x*TILE_SIZE),
         top_left_y + (y*TILE_SIZE)- (image.get_height()))
        )
    
def draw_shadow(image,y,x):
    screen.blit(
        image,
        (top_left_x+(x*TILE_SIZE),
         top_left_y+(y*TILE_SIZE))
    )

def draw_player():
    player_image = PLAYER[player_direction][player_frame]
    draw_image(player_image,player_y + player_offset_y, player_x+player_offset_x)
    player_image_shadow = PLAYER_SHADOW[player_direction][player_frame]
    draw_shadow(player_image_shadow,player_y + player_offset_y, player_x+player_offset_x)

def draw():
    if game_over:
        return
    #Clear  game window
    box=Rect((0,150),(800,600))
    screen.draw.filled_rect(box,RED)
    box= Rect((0,0), (800, int(top_left_y + (room_height-1)*TILE_SIZE)))
    screen.surface.set_clip(box)
    floor_type =get_floor_type()
                   # draw floor tiles, items
    for y in range(room_height):
        for x in range(room_width):
            draw_image(objects[floor_type][0],y,x)
            if room_map[y][x] in items_player_may_stand_on:
                draw_image(objects[room_map[y][x]][0],y,x)

    #Pressure Pad on room 26
    if current_room == 26:
        draw_image(objects[39][0],8,2)
        image_on_pad =room_map[8][2]
        if image_on_pad >0:
           draw_image(objects[image_on_pad][0],8,2)
    for y in range(room_height):
        for  x in range(room_width):
            item_here=room_map[y][x]
            if item_here not in items_player_may_stand_on + [255]:
                image = objects[item_here][0]

            
                if (current_room in outdoor_rooms
                    and y == room_height - 1
                    and room_map[y][x] == 1) or \
                    ( current_room not in outdoor_rooms
                    and y == room_height - 1
                    and room_map[y][x] == 1
                    and x >0
                    and x < room_width -1):
                    #add transparent wall image in the front row.
                    image=PILLARS[wall_transparency_frame]

                draw_image(image,y,x)

                if objects[item_here][1] is not None:
                     shadow_image = objects[item_here][1]
                     if shadow_image in [images.half_shadow,
                                         images.full_shadow]:
                           shadow_width=int(image.get_width() /TILE_SIZE)
                           for z in range(0, shadow_width):
                              draw_shadow(shadow_image,y,x+z)
                     else:
                        draw_shadow(shadow_image,y,x)

            hazard_here=hazard_map[y][x]
            if hazard_here != 0:
                draw_image(objects[hazard_here][0],y,x)
                
            if(player_y ==y):
                draw_player()

            
    ###end of for loop
    screen.surface.set_clip(None)
########
#   AIR
#######

def draw_energy_air():
    box = Rect((20,765), (350,20))
    screen.draw.filled_rect(box, BLACK)
    screen.draw.text("AIR",(20,766), color= BLUE)
    screen.draw.text("ENERGY", (180,766), color = YELLOW)

    if air>0:
        box =Rect((50,765), (air,20))
        screen.draw.filled_rect(box,BLUE)
    if energy >0:
        box = Rect((250,765),(energy,20))
        screen.draw.filled_rect(box,YELLOW)




    
def end_the_game(reason):
    global game_over
    print( "Ending game")
    show_text(reason ,1)
    game_over= True
    sounds.gameover.play()
    screen.draw.text("GAME OVER", (120,400), color = "white", fontsize = 128, shadow = (1,1) , scolor = "black")

def air_countdown():
    global air, game_over
    if game_over:
        return
    air -=1
    if air == 20:
        sounds.say_air_low.play()
    if air == 10:
        sounds.say_act_now.play()
    draw_energy_air()
    if air<1:
        end_the_game("You're out of air!")

def alarm():
    show_text("air is running our, " + PLAYER_NAME + "! Get to safety, then radio for help!", 1)
    sounds.alarm.play(3)
    sounds.say_breach.play()
    
def deplete_energy(penalty):
    global energy, game_over
    if game_over:
        return
    energy = energy-penalty
    draw_energy_air()
    if energy<1:
        end_the_game("You're out of energy!")
def hazard_start():
    global current_room_hazards_list,hazard_map
    if current_room in hazard_data.keys():
        current_room_hazards_list = hazard_data[current_room]
        for hazard in current_room_hazards_list:
            hazard_y = hazard[0]
            hazard_x = hazard[1]
            hazard_map[hazard_y][hazard_x] =49 + (current_room % 3)
        clock.schedule_interval(hazard_move,0.15)

def hazard_move():
    global current_room_hazards_list,hazard_data,hazard_map
    global old_player_x,old_player_y

    if game_over:
        return
    for hazard in current_room_hazards_list:
        hazard_y = hazard[0]
        hazard_x = hazard[1]
        hazard_direction = hazard[2]
        
        old_hazard_x = hazard_x
        old_hazard_y = hazard_y
        hazard_map[old_hazard_y][old_hazard_x] = 0 
            
        if hazard_direction == 1: # up
            hazard_y -= 1
        if hazard_direction == 2: # right
            hazard_x += 1
        if hazard_direction == 3: # down
            hazard_y += 1
        if hazard_direction == 4: # left
            hazard_x -= 1

        hazard_should_bounce = False

        if (hazard_y == player_y and hazard_x == player_x) or \
           (hazard_y == from_player_y and hazard_x == from_player_x
            and player_frame > 0):
            sounds.ouch.play()
            deplete_energy(1)
            hazard_should_bounce = True
            
         # Stop hazard going out of the doors
        if hazard_x == room_width: 
            hazard_should_bounce = True
            hazard_x = room_width - 1
        if hazard_x == -1: 
            hazard_should_bounce = True
            hazard_x = 0
        if hazard_y == room_height:
            hazard_should_bounce = True
            hazard_y = room_height - 1
        if hazard_y == -1:
            hazard_should_bounce = True
            hazard_y = 0

        # Stop when hazard hits scenery or another hazard.
        if room_map[hazard_y][hazard_x] not in items_player_may_stand_on \
               or hazard_map[hazard_y][hazard_x] != 0:
            hazard_should_bounce = True
            
        if hazard_should_bounce:
            hazard_y = old_hazard_y # Move back to last valid position.
            hazard_x = old_hazard_x
            hazard_direction += hazard[3]
            if hazard_direction > 4:
                hazard_direction -= 4
            if hazard_direction < 1:
                hazard_direction += 4
            hazard[2] = hazard_direction

        hazard_map[hazard_y][hazard_x] = 49 + (current_room % 3)
        hazard[0] = hazard_y
        hazard[1] = hazard_x
        

def adjust_wall_transparency():
    global  wall_transparency_frame

    if (player_y == room_height-2
        and room_map[room_height-1][player_x] == 1
        and int(wall_transparency_frame) <4):
      wall_transparency_frame += 1 # fade the wall out
    if ((player_y <room_height-2
        or room_map[room_height-1][player_x] !=1)
        and int(wall_transparency_frame) >0):
      wall_transparency_frame -= 1 #fade the wall in

def show_text(text_to_show,line_number):
    if game_over:
        return
    text_lines=[15,50]
    box = Rect(( 0,text_lines[line_number]),(800,35))
    screen.draw.filled_rect(box,BLACK)
    screen.draw.text(text_to_show,(20,text_lines[line_number]), color=GREEN)

    

####
## PROPS
#################

# Props are objects that may move between rooms, appear or disappear.
# All props must be set up here. Props not yet in the game go into room 0.
# object number : [room_number, y, x]
props = {
    20: [31, 0, 4], 21: [26, 0, 1], 22: [41, 0, 2 ], 23: [39, 0, 5],
    24: [45, 0, 2],
    25: [32, 0, 2], 26: [27, 12, 5], # two sides of same door
    40: [0, 8, 6], 53: [45, 1, 5], 54: [0, 0, 0], 55: [0, 0, 0],
    56: [0, 0, 0], 57: [35, 4, 6], 58: [0, 0, 0], 59: [31, 1, 7],
    60: [0, 0, 0], 61: [36, 1, 1], 62: [36, 1, 6], 63: [0, 0, 0],
    64: [27, 8, 3], 65: [50, 1, 7], 66: [39, 5, 6], 67: [46, 1, 1],
    68: [0, 0, 0], 69: [30, 3, 3], 70: [47, 1, 3],
    71: [0, LANDER_Y, LANDER_X], 72: [0, 0, 0], 73: [27, 4, 6], 
    74: [28, 1, 11], 75: [0, 0, 0], 76: [41, 3, 5], 77: [0, 0, 0],
    78: [35, 9, 11], 79: [26, 3, 2], 80: [41, 7, 5], 81: [29, 1, 1]
    }

checksum=0
for key, prop in props.items():
    if key != 71:
        checksum += (prop[0]*key+ prop[1]*(key+1)+prop[2]*(key+2))
print(len(props), "props")
assert len(props) ==37, "Expected 27 propitems"
print("Prop checksum:", checksum)
assert checksum  == 61414, "Error in props data"


####what I am carrying when the game starts
in_my_pockets = [55]
#in_my_pockets = [55,73,74]

selected_item = 0
item_carrying = in_my_pockets[selected_item]

###used to combine object to create a new one 
RECIPES = [
    [62, 35, 63], [76, 28, 77], [78, 38, 54], [73, 74, 75],
    [59, 54, 60], [77, 55, 56], [56, 57, 58], [71, 65, 72],
    [88, 58, 89], [89, 60, 90], [67, 35, 68], [63, 67, 68]
    ]

checksum = 0
check_counter = 1
for recipe in RECIPES:
    checksum += (recipe[0] * check_counter
                 + recipe[1] * (check_counter + 1) 
                 + recipe[2] * (check_counter + 2))
    check_counter += 3
print(len(RECIPES), "recipes")
assert len(RECIPES) == 12, "Expected 11 recipes"

print("Recipe checksum:", checksum)
assert checksum == 44231, "Error in recipes data"

####using props

def find_object_start_x():
    checker_x =player_x
    while room_map[player_y][checker_x] == 255:
        checker_x -= 1
    return checker_x

def get_item_under_player():
    item_x =find_object_start_x()
    item_player_is_on = room_map[player_y][item_x]
    return item_player_is_on


#pick up


def pick_up_object():
     global room_map
     item_player_is_on = get_item_under_player()
     if item_player_is_on in items_player_may_carry:
         room_map[player_y][player_x] = get_floor_type()
         add_object(item_player_is_on)
         show_text( "Now Carrying " + objects[item_player_is_on][3],0)
         ### remove object from scenery map
         sounds.pickup.play()
         time.sleep(0.5)
     else:
        show_text("You can't carry that!",0)


def add_object(item): ### add to inventory
    global selected_item, item_carrying
    in_my_pockets.append(item)
    item_carrying = item
    selected_item = len(in_my_pockets) - 1
    display_inventory()
    print( " props now in room 0")
    props[item][0]=0
    # carried object are in room zero -- off map
    print (props)

def display_inventory():
    box = Rect((0,45),(800,105))
    screen.draw.filled_rect(box, BLACK)

    if len(in_my_pockets) ==0:
        return
         
    start_display =( selected_item//16) *16
    list_to_show = in_my_pockets[start_display: start_display +16]
    selected_marker =selected_item % 16

    for item_counter in range(len(list_to_show)):
        item_number = list_to_show[item_counter]
        image =objects[item_number][0]
        screen.blit(image, (25+(46* item_counter),90))



    box_left = (selected_marker *46) -3
    box= Rect((22 + box_left,85),(40,40))
    screen.draw.rect(box,WHITE)
    item_highlighted = in_my_pockets[selected_item]
    description =objects[item_highlighted][2]
    screen.draw.text(description,(20,130), color = "white")
                     

# drop

def drop_object(old_y,old_x):
    global room_map, props
    if room_map[old_y][old_x] in[0,2,39]: #place where you can drop
        props[item_carrying][0] = current_room
        props[item_carrying][1] = old_y
        props[item_carrying][0] = old_x
        room_map[old_y][old_x] = item_carrying
        show_text ("You have dropped " + objects[item_carrying][3],0)
        sounds.drop.play()
        remove_object(item_carrying)
        time.sleep(0.5)
    else:
        show_text("You can't drop that there.",0)
        time.sleep(0.5)


def remove_object(item):
    global selected_item, in_my_pockets, item_carrying
    in_my_pockets.remove(item)
    selected_item=selected_item-1
    if selected_item <0:
        selected_item =0
    if len(in_my_pockets) == 0:
        item_carrying = False
    else:
        item_carrying=in_my_pockets[selected_item]
    display_inventory()

def examine_object():
    item_player_is_on = get_item_under_player()
    left_tile_of_item = find_object_start_x()
    if item_player_is_on in [0,2]:
        return
    description = "You see: " + objects[item_player_is_on][2]
    for prop_number, details in props.items():
        if details[0] == current_room:
           if (details[1] == player_y
               and details[2] == left_tile_of_item
               and room_map[details[1]][details[2]] != prop_number):
               add_object(prop_number)
               description ="You found " + objects[prop_number][3]
               sounds.combine.play()
    show_text(description,0)
    time.sleep(0.5)

def use_object():
    global room_map, props, item_carrying, air, selected_item,energy
    global in_my_pockets, suit_stiched, air_fixed, game_over

    use_message = "You fiddle around with it but don't get anywhere."
    standard_responses = {
        4: "Air is running out! you can't take this lying down!",
        6: "This is no time to sit around!",
        7: "This is no time to sit around!",
        32: "It shakes and rumbles, but nothing else happens.",
        34: "Ah! That's better. Now wash your hands.",
        35: "You wash your hands and shake the water off.",
        37: "The test tubes smoke slightly as you shake them.",
        43: "A Whiteboard with data experiment",
        54: "You chew the gum. It's sticky like glue.",
        55: "The yoyo bounces up and down, slightly slower than on Earth",
        56: "It's a bit too fiddly. Can you thread it on something?",
        59: "You need to fix the leak before you can use the canister",
        61: "You try signalling with the mirror, but nobody can see you.",
        62: "Don't throw resources away. Things might come in handy...",
        67: "To enjoy yummy space food, just add water!",
        75: "You are at Sector: " + str(current_room) + " // X: " \
            + str(player_x) + " // Y: " + str(player_y)  
        }

    #get object number at player's location
    item_player_is_on = get_item_under_player()
    print ( "the item the user is on is " , item_player_is_on)
    for this_item in [item_player_is_on, item_carrying]:
        if this_item in standard_responses:
            use_message = standard_responses[this_item]


    if item_carrying == 70 or item_player_is_on == 70:
        use_message = "Banging tune!"
        sounds.steelmusic.play(2)
    elif item_player_is_on == 11:
        use_message = "AIR: " + str(air) + "%/ENERGY" + str(energy) + "%/"
        if not suit_stiched:
            use_message += "* ALERT* SUIT FABRIC TORN/"
        if not air_fixed:
            use_message += "* ALERT* SUIT AIR BOTTLE MISSING/"
        if suit_stiched and air_fixed:
            use_message += " SUIT OK"#status update when player on PC
            show_text(use_message,0)
            sounds.say_status_report.play()
            time.sleep(0.5)
            return

    elif item_carrying ==60 or item_player_is_on == 60:
       use_message = "you fix " + objects[60][3] + " to the suit!"
       air_fixed =True
       air=90
       air_countdown()
       remove_object(60)
    elif (item_carrying ==58 or item_player_is_on ==58) and not suit_stiched:
        
        use_message = "You radio for help. A rescue ship is coming. Rendevouz Sector 12, outside."
        props[40][0] =13
    elif (item_carrying == 66 or item_player_is_on ==66) and current_room in outdoor_rooms:
        use_messgae = " you dig..."
        if (current_room == LANDER_SECTOR and player_x== LANDER_X and player_Y == LANDER_Y):
            add_object(71)
            use_message = "You found the Poodle lander!"
    elif item_player_is_on == 40:
        clock.unschedule(air_countdown)
        show_text("Congratulations, " + PLAYER_NAME + "!", 0)
        show_text("Missing success! You have made it to safety.", 1)
        game_over = True
        sounds.take_off.play()
        game_completion_sequence()
    elif item_player_is_on == 16:
        energy +=1
        if energy >100:
            energy =100
            use_message = "You munch the lettuce and get a little energy back"
            draw_energy_air()
    elif item_player_is_on ==42:
        if current_room == 27:
            open_door(26)
        props[25][0] = 0
        props[26][0] =0
        clock.schedule_unique(shut_engineering_door,60)
        use_message = "You press the button"
        show_text("Door to engineering bay is open for 60 seconds" , 1)
        sounds.doors.play()
    elif item_carrying == 68 or item_player_is_on ==68:
        energy = 100
        use_message = "You use the food to restore your energy"
        remove_object(68)
        draw_energy_air()

    if suit_stiched and air_fixed:
        if current_room ==31 and props[20][0] ==31:
            open_door(20) #which include removing door
            sounds.say_airlock_open.play()
            show_text("The computer tells you the airlock is now open.",1)
        elif props[20][0] == 31:
            props[20][0] ==0 #remove door form map
            sounds.say_airlock_open.play()
            show_text("The computer tells you the airlock is now open.",1) 
        
    for recipe in RECIPES:
        ingredient1= recipe[0]
        ingredient2= recipe[1]
        combination= recipe[2]
        #print( " checking now " , ingredient1, ingredient2, combination)
        if (item_carrying == ingredient1 and item_player_is_on == ingredient2)\
           or (item_carrying == ingredient2 and item_player_is_on == ingredient1):
                use_message = " You combine " + objects[ingredient1][3] + " and "  + " to make " + objects[combination][3]
            
                if item_player_is_on in props.keys():
                    props[item_player_is_on][0] =0
                    room_map[player_y][player_x] = get_floor_type()
                in_my_pockets.remove(item_carrying)
                add_object(combination)
                print( " the object is combined")
                sounds.combine.play()

#{key objectnumber:door object number }
## ACCESS DICTIONARY
    ACCESS_DICTIONARY = {79:22, 80:23, 81:24}
    if item_carrying in ACCESS_DICTIONARY:
        door_number = ACCESS_DICTIONARY[item_carrying]
        if props[door_number][0] == current_room:
            use_message =  "You unlock the door!"
            sounds.say_doors.play()
            sounds.doors.play()
            open_door(door_number)
            

    show_text(use_message,0)
    time.sleep(0.5)

def game_completion_sequence():
    global launch_frame
    box = Rect((0,150),(800,600))
    screen.draw.filled_rect(box,(128,0,0))
    box = Rect ((0,top_left_y-30),(800,390))
    screen.surface.set_clip(box)

    for y in range(0,13):
        for x in range(0,13):
            draw_image(iamges.soil,y,x)
    launch_frame +=1
    if launch_frame<9:
        draw_image(images.rescue_ship,8 - launch_frame,6)
        clock.schedule(game_completion_sequence,0.25)
    else:
        screen.surface.set_clip(None)
        screen.draw.text("MISSION", (200,380), color = "white",
                         fontsize =128, showdow =(1,1) , scolor="black")
        screen.draw.text("COMPLETE", (145,480), color = "white",
                         fontsize =128, showdow =(1,1) , scolor="black")
        sounds.completion.play()
        sounds.say_mission_complete.play()
        
    

############
# DOOR
################
def open_door(opening_door_number):
    global door_frames, door_shadow_frames
    global door_frame_number, door_object_number
    door_frames = [images.door1, images.door2, images.door3, images.door4, images.floor]
    #final frame restore shadow
    door_shadow_frames =[images.door1_shadow, images.door2_shadow, images.door3_shadow, images.door4_shadow, images.door_shadow]
    door_frame_number=0
    door_object_number=opening_door_number
    do_door_animation()
    
def close_door(opening_door_number):
    global door_frames, door_shadow_frames
    global door_frame_number, door_object_number
    door_frames = [images.door4, images.door3, images.door2, images.door1, images.floor]
    #final frame restore shadow
    door_shadow_frames =[images.door4_shadow, images.door3_shadow, images.door2_shadow, images.door1_shadow, images.door_shadow]
    door_frame_number=0
    door_object_number=closing_door_number
    if player_y ==props[door_object_number][1]:
        if player_y == 0: #if in top doorway
            player_y =1 #move them down
        else:
            player_y = room_height -2
    do_door_animation()
    
def do_door_animation():
    global door_frames, door_frame_number, door_object_number, objects
    objects[door_object_number][0] = door_frames[door_frame_number]
    objects[door_object_number][1] = door_shadow_frames[door_frame_number]
    door_frame_number += 1
    if door_frame_number ==5:
        if door_frames[-1] == images.floor:
            props[door_object_number][0] =0 #remove door from props
        #redo map
        generate_map()
    else:
        clock.schedule(do_door_animation,0.15)

def shut_engineering_door():
    global current_room, door_room_number, props
    props[25][0] = 32  #Door from room32 to the engineering bay
    props[26][0] = 27  #Door inside engineering bay
    generate_map()
    if current_room == 27:
        close_door(26)
    if current_room == 32:
        close_door(25)
    show_text("The computer tells yu the door are closed.",1)
    sounds.say_doors_closed.play()

def door_in_room_26():
    global airlock_door_frame,room_map

    frames = [images.door, images.door1, images.door2,images.door3, images.door4, images.floor]
    shadow_frames = [images.door_shadow, images.door1_shadow, images.door2_shadow,images.door3_shadow, images.door4_shadow, None]
    if current_room != 26:
        clock.unschedule(door_in_room_26)
        return
    #prop 21 is the door in Room 26
    if ((player_y ==8 and player_x ==2) or props[63] == [26,8,2]) and props[21][0] == 26:
        airlock_door_frame += 1
        if airlock_door_frame ==5:
            props[21][0] =0 #Remove door
            room_map[0][1]=0
            room_map[0][2]=0
            room_map[0][3]=0
    if (( player_y !=8 or player_x != 2) and props[63] != [26,8,2]) and airlock_door_frame >0:
        if airlock_door_frame  == 5:
            props[21][0] =26 # add door
            room_map[0][1]=21
            room_map[0][2]=255
            room_map[0][3]=255
        airlock_door_frame -= 1
    objects[21][0]= frames[airlock_door_frame]
    objects[21][1] = shadow_frames[airlock_door_frame]


###############
##  HAZARDS  ##
###############

hazard_data = {

    # room number: [[y, x, direction, bounce addition to direction]]
    28: [[1, 8, 2, 1], [7, 3, 4, 1]], 32: [[1, 5, 4, -1]],
    34: [[5, 1, 1, 1], [5, 5, 1, 2]], 35: [[4, 4, 1, 2], [2, 5, 2, 2]],
    36: [[2, 1, 2, 2]], 38: [[1, 4, 3, 2], [5, 8, 1, 2]],
    40: [[3, 1, 3, -1], [6, 5, 2, 2], [7, 5, 4, 2]],
    41: [[4, 5, 2, 2], [6, 3, 4, 2], [8, 1, 2, 2]],
    42: [[2, 1, 2, 2], [4, 3, 2, 2], [6, 5, 2, 2]],
    46: [[2, 1, 2, 2]],
    48: [[1, 8, 3, 2], [8, 8, 1, 2], [3, 9, 3, 2]]
    }


####
## START
##################
      
clock.schedule_interval(game_loop, 0.03)
generate_map()
clock.schedule_interval(adjust_wall_transparency,0.05)
clock.schedule_unique(display_inventory,1)
clock.schedule_unique(draw_energy_air,0.5)
clock.schedule_unique(alarm,10)
clock.schedule_interval(air_countdown,5)
sounds.mission.play()


























    
