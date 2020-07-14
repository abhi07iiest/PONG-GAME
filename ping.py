import pygame,sys,random

def ball_animation():
     global ball_speed_x,ball_speed_y,player1_score,player2_score,timer
     ball.x += ball_speed_x
     ball.y += ball_speed_y
     if ball.top <=0 or ball.bottom >= screen_height:
          ball_speed_y *= -1
     if ball.left <=0:
          pygame.mixer.Sound.play(score_sound)

          player1_score += 1
          timer = pygame.time.get_ticks()



     if ball.right >= screen_width:
          pygame.mixer.Sound.play(score_sound)

          player2_score += 1
          timer = pygame.time.get_ticks()


     if ball.colliderect(player1) and ball_speed_x > 0:
         pygame.mixer.Sound.play(pong_sound)
         if abs(ball.right-player1.left) < 10:
             ball_speed_x *= -1
         elif abs(ball.bottom-player1.top) < 10 and ball_speed_y > 10:
             ball_speed_y *= -1
         elif abs(ball.top-player1.bottom) < 10 and ball_speed_y < 10:
             ball_speed_y *= -1


     if ball.colliderect(player2) and ball_speed_x < 0:
          pygame.mixer.Sound.play(pong_sound)

          if abs(ball.left-player2.right) < 10:
              ball_speed_x *= -1
          elif abs(ball.bottom-player2.top) < 10 and ball_speed_y > 10:
              ball_speed_y *= -1
          elif abs(ball.top-player2.bottom) < 10 and ball_speed_y < 10:
              ball_speed_y *= -1




def player1_animation():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2_animation():
        global ball_speed_x,ball_speed_y
        if ball.y > player2.y:
            player2.y +=pl_speed
        if ball.y < player2.y:
            player2.y -= pl_speed
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_height:
            player2.bottom = screen_height

def ball_restart():
        global ball_speed_x,ball_speed_y,timer,player1_score,player2_score
        current_time = pygame.time.get_ticks()
        ball.center = (screen_width/2,screen_height/2)
        if player1_score ==2:

            if current_time-timer < 2000:
                 text1 = game_font2.render("YOU   WIN",False,light_gray)
                 screen.blit(text1,(200,200))
            else:

             player1_score = 0
             player2_score = 0

        if player2_score ==2:

            if current_time-timer < 2000:
              text2 = game_font2.render("YOU LOOSE",False,light_gray)
              screen.blit(text2,(200,200))
            else:
             player1_score = 0
             player2_score = 0
        if current_time-timer < 1000:
            number3 = game_font.render("3",False,light_gray)
            screen.blit(number3,(480,300))
        if 1000< current_time-timer < 2000:
           number2 = game_font.render("2",False,light_gray)
           screen.blit(number2,(480,300))
        if 2000< current_time-timer < 3000:
            number1 = game_font.render("1",False,light_gray)
            screen.blit(number1,(480,300))
        if current_time-timer < 3000:
            ball_speed_x,ball_speed_y = 0,0


        else:
            ball_speed_y = 10*random.choice((1,-1))
            ball_speed_x  = 10*random.choice((1,-1))
            timer = None






pygame.init()
clock = pygame.time.Clock()





 #main window
screen_width = 980
screen_height = 560

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('ping pong')

#players and material
ball = pygame.Rect(screen_width/2-10,screen_height/2-10,30,30)
player1 = pygame.Rect(screen_width-10,screen_height/2-70,20,140)
player2 = pygame.Rect(0,screen_height/2-70,10,140)

bg_color = pygame.Color('blue')
light_gray = (200,200,200)
red = (255,0,0)
orange = (255,165,0)
green = (0,255,0)

ball_speed_x = 10
ball_speed_y = 10
player_speed = 0
pl_speed = 8

# score variable
player1_score = 0
player2_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)
game_font2 = pygame.font.Font("freesansbold.ttf",100)


#timer
timer = True

#sound

pong_sound = pygame.mixer.Sound('pong.ogg')
score_sound = pygame.mixer.Sound('score.ogg')

while 1:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
                 player_speed += 10
             if event.key == pygame.K_UP:
                player_speed -= 10
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_DOWN:
                player_speed -= 10
             if event.key == pygame.K_UP:
                player_speed += 10

     ball_animation()
     player1_animation()
     player2_animation()



     screen.fill(bg_color)
     pygame.draw.rect(screen,green,player1)
     pygame.draw.rect(screen,red,player2)
     pygame.draw.ellipse(screen,orange,ball)

     pygame.draw.aaline(screen,light_gray,(screen_width/2,0),(screen_width/2,screen_height))

     if timer:
         ball_restart()
     player1_text = game_font.render(f"{player1_score}",False,light_gray)
     player2_text = game_font.render(f"{player2_score}",False,light_gray)

     screen.blit(player1_text,(510,250))
     screen.blit(player2_text,(450,250))





     pygame.display.flip()
     clock.tick(60)
