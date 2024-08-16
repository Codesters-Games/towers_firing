# sprite = codesters.Rectangle(x, y, width, height, "color")
path_middle = codesters.Rectangle(0, 0, 100, 500, "blue")
path_left = codesters.Rectangle(-200, 0, 300, 500, "grey")
path_right = codesters.Rectangle(200, 0, 300, 500, "grey")
soccernet = codesters.Sprite("soccernet", 0, 200)
soccernet.flip_right_left()
player = codesters.Sprite("athlete1", 0, -200)
soccernet.set_size(0.3)
player.set_size(0.2)
shots_arr = []

stage.disable_all_walls()

def up_key():
    player.move_up(10)
def down_key():
    player.move_down(10)

def collision(sprite, hit_sprite):
    my_var = hit_sprite.get_image_name() 
    if my_var == "soccernet":
        sprite.say("VICTORY!")
        stage.event_interval(None)
        stage.remove_all_sprite_events()

stage.event_key("down", down_key)
stage.event_key("up", up_key)
player.event_collision(collision)


def sub(v, u):
    return [ u[0]-v[0], u[1]-v[1] ]

# caluculate the length of a vector
# this is the Pythagorean Theorem 
# h length = square root of ( x squared plus y squared)
def magnitude(v):
    return math.sqrt( v[0]*v[0] + v[1]*v[1] )
    
# multiply this vector by the number s
def multiply(v, s):
    return [ v[0]*s, v[1]*s ]
    
# divide this vector by the number s
def divide(v, s):
    if s == 0:  # can't divide by zero!
        return v
    return [ v[0]/s, v[1]/s ]

# make this vector length 1
# divide it by its magnitude
def normalize(v):
    mag = magnitude(v)
    return divide(v, mag)

def collision_for_shot(sprite, hit_sprite):
    # if the shot hit any wall, remove the shot to save memory
    # if hit_sprite == south_wall or hit_sprite == north_wall or hit_sprite == east_wall or hit_sprite == west_wall:
    #     stage.remove_sprite(sprite)
    #     sprite.pen_clear()
    if hit_sprite == player:
        stage.remove_sprite(sprite)
        sprite.pen_clear()
        hit_sprite.say("GAME OVER!")
        stage.event_interval(None)
        stage.remove_all_sprite_events()

def shoot(shooter, target):
    global shots_arr
    
    if len(shots_arr)>0:
        shots_arr[0].pen_clear()
        shots_arr.clear()
        
    # get a vector for the position of the shooter
    v = [shooter.get_x(),shooter.get_y()]
    # get a vector for the position of the target
    u = [target.get_x(), target.get_y()]
    # subtract and get the vector from the shooter to
    # the target. I will use dir to set the
    # x and y speed of a shot that will go to the target
    dir = sub(v, u)
    # make a shot starting at the shooter
    shot = codesters.Circle(shooter.get_x(), shooter.get_y(), 7, "red")
    shots_arr.append(shot)
    
    # n is our normalized dir
    n = normalize(dir)
    # s will be our speed vector
    s = multiply(n, 10)
    shot.set_x_speed(s[0])
    shot.set_y_speed(s[1])
    # shot.pen_down()
    shot.event_collision(collision_for_shot)
    
    
iron_man1 = codesters.Sprite("costumed_person1",-130, 160)
iron_man1.set_size(0.3)

iron_man2 = codesters.Sprite("costumed_person1",200, 150)
iron_man2.set_size(0.3)

iron_man3 = codesters.Sprite("costumed_person1",-200, -50)
iron_man3.set_size(0.3)

def interval():
    shoot(iron_man1,player)
    shoot(iron_man2,player)
    shoot(iron_man3,player)
    

# every 2 seconds, the shooter shoots at the target,
stage.event_interval(interval, 1.5)

