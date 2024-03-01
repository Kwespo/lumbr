import pygame
import random
import tree as tree_F
import player as player_F
import DEBUG as dbg

# --- Game States ---
menuVisable = False
debugMenuVisable = False

def make_Trees(treeDensityPersentage, mapX, mapY, screen):
  # ---- Creating forest -----
  
  # Tree entities
  treeS = tree_F.Tree()
  treeImg = treeS.sprite

  #Tree denciy = area of map / density of trees
  treeDensity = (((mapX//2) * (mapY//2)) // 100) * treeDensityPersentage

  for tree in range(0,treeDensity):
    if tree == treeDensity:
      if dbg.debug:
        dbg.log(f'Finished creating Trees...\nTree dencity: {treeDensity}\nTree location: {treeS.trees}\nTree sprite: {treeS.sprite}\n')
      break

    treeS.create(random.randint(0, mapX-16), random.randint(0, mapY-16))
    screen.blit(treeImg, (treeS.x, treeS.y))
    tree_F.Tree.trees.append([(treeS.x, treeS.y), treeS])

  return treeS, treeImg

def show_Menu(key):
  global menuVisable, debugMenuVisable
  dbg.log(f"menu is: {menuVisable} and debug is {debugMenuVisable}")
  if key == pygame.K_c:
    dbg.log(f"menu is: {menuVisable} but is turning to {not menuVisable}")
    menuVisable = not menuVisable
    dbg.log(f"menu is: {menuVisable} and debug is {debugMenuVisable}")
  elif key == pygame.K_a:
    dbg.log(f"debugging is: {debugMenuVisable} but is turning to {not debugMenuVisable}")
    debugMenuVisable = not debugMenuVisable
    


def display_Screen(mapX = 700, mapY = 600, title = 'Lumbr', treeDensityPersentage = 10):
  # ----- Global Vars -----
  global menuVisable,debugMenuVisable

  # ----- Pygame setup  -----
  pygame.init()
  fps = 30
  font = pygame.font.SysFont('comic sans', 30)
  clock = pygame.time.Clock()
  pygame.display.set_caption(title)
  

# ----- Screen setup -----
  screen = pygame.display.set_mode((mapX, mapY))
  screen.fill((50,205,50))
  if dbg.debug:
      dbg.log(f'Creating screen...\nScreen size: {mapX, mapY}\nScreen title: {title}\nfps {fps}\nFont: {font}\nclock: {clock}\n')

  # ---- Creating forest -----
  treeImg = make_Trees(treeDensityPersentage, mapX, mapY, screen)[1] # Returns treeImg
  

# ---- Player setup ----
  playerS = player_F.Player()
  playerImg = playerS.sprite
  playerS.create(mapX // 2, mapY // 2) # Spawns in the middle of the screen
  screen.blit(playerImg, (playerS.x, playerS.y))

# ----- Main loop -----
  running = True
  while running:

    screen.fill((50,205,50))
    if len(tree_F.Tree.trees) == 0:
      make_Trees(treeDensityPersentage, mapX, mapY, screen)
    else:
      for i in range(len(tree_F.Tree.trees)):
        screen.blit(treeImg, tree_F.Tree.trees[i][0])
    screen.blit(playerImg, (playerS.x, playerS.y))
    if menuVisable:
      text = font.render('Controls:', 1, (255,255,255))
      screen.blit(text, (10,10))
      text = font.render('Arrow Keys to move', 1, (255,255,255))
      screen.blit(text, (10,40))
      text = font.render('Space to chop tree', 1, (255,255,255))
      screen.blit(text, (10,70))
      text = font.render('ESC to quit', 1, (255,255,255))
      screen.blit(text, (10,100))
    elif debugMenuVisable:
      text = font.render('SHOWWING', 1, (255,255,255))
      text.blit(text, (10,10))
    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
      #Logs the event
      if dbg.debug:
        dbg.log(f'Event: {event}\n')

      #Quits the game
      if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
      
      #Player action
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c or event.key == pygame.K_a:
          dbg.log(f"Key: {pygame.KEYDOWN} \n")
          show_Menu(event.key)
        else:
          playerS.playerAction(pygame.key.get_pressed(), mapX, mapY)