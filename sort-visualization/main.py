import pygame
import random
import math
pygame.init()

class Data:
  BLACK = 0, 0, 0
  RED = 255, 0, 0
  BACKGROUND_COLOR = 255, 255, 255

  FONT = pygame.font.SysFont('Arial', 20)
  LARGE_FONT = pygame.font.SysFont('Arial', 30)

  SIDE = 100
  TOP = 150

  def __init__(self, width, height, lst):
    self.width = width
    self.height = height
    icon = pygame.image.load('logo.png')
    pygame.display.set_icon(icon)
    self.window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vizualizacija sorting algoritama")
    
    self.setList(lst)

  def setList(self, lst):
    self.lst = lst
    self.min = min(lst)
    self.max = max(lst)

    self.blockWidth = round((self.width - self.SIDE) / len(lst))
    self.blockHeight = math.floor((self.height - self.TOP) / (self.max - self.min))
    self.startX = self.SIDE // 2

def draw(data, algorythm, ascending):
  data.window.fill(data.BACKGROUND_COLOR)

  title = data.LARGE_FONT.render(f"{algorythm} > {'Neopadajuci' if ascending else 'Nerastuci'}", 1, data.RED)
  data.window.blit(title, (data.width/2 - title.get_width()/2 , 5))

  controls = data.FONT.render("R - Reset | SPACE - Sort | STRELICA KA GORE - Neopadajuci | STRELICA KA DOLE - Nerastuci", 1, data.BLACK)
  data.window.blit(controls, (data.width/2 - controls.get_width()/2 , 45))

  sorting = data.FONT.render("I - Insertion Sort | B - Bubble Sort | Uskoro vise", 1, data.BLACK)
  data.window.blit(sorting, (data.width/2 - sorting.get_width()/2 , 75))

  drawList(data)
  pygame.display.update()

def drawList(data, clearBg=False, colors=[]):
  lst = data.lst
  generateColors(lst, colors)
  if clearBg:
    clearRect = (data.SIDE//2, data.TOP, data.width - data.SIDE, data.height - data.TOP)
    pygame.draw.rect(data.window, data.BACKGROUND_COLOR, clearRect)
  j = 0
  for i, val in enumerate(lst):
    x = data.startX + i * data.blockWidth
    y = data.height - (val - data.min) * data.blockHeight

    pygame.draw.rect(data.window, colors[j], (x, y, data.blockWidth, data.height))
    j += 1
  if clearBg:
    pygame.display.update()

def generateArray(n, min, max):
  lst = []

  for _ in range(n):
    val = random.randint(min, max)
    lst.append(val)

  return lst

def generateColors(lst, colors):
  for e in range(0, len(lst)):
    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def bubbleSort(data, ascending=True):
  lst = data.lst

  for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
      num1 = lst[j]
      num2 = lst[j + 1]

      if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        drawList(data, True)
        yield True

  return lst

def insertionSort(data, ascending=True):
  lst = data.lst

  for i in range(1, len(lst)):
    current = lst[i]

    while True:
      aSort = i > 0 and lst[i - 1] > current and ascending
      dSort = i > 0 and lst[i - 1] < current and not ascending

      if not aSort and not dSort:
        break

      lst[i] = lst[i - 1]
      i = i - 1
      lst[i] = current
      drawList(data, True)
      yield True

  return lst


def main():
  run = True
  clock = pygame.time.Clock()

  n = 50
  min = 0
  max = 100

  lst = generateArray(n, min, max)
  data = Data(1000, 800, lst)
  sorting = False
  ascending = True
  
  sortingAlgorithm = bubbleSort
  _sortingAlgorythm = "Bubble Sort"
  algGen = None

  while run:
    clock.tick(60)

    if sorting:
      try:
        next(algGen)
      except StopIteration:
        sorting = False
    else:
      draw(data, _sortingAlgorythm, ascending)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type != pygame.KEYDOWN:
        continue

      if event.key == pygame.K_r:
        lst = generateArray(n, min, max)
        data.setList(lst)
        sorting = False
      elif event.key == pygame.K_SPACE and sorting == False:
        sorting = True
        algGen = sortingAlgorithm(data, ascending)
      elif event.key == pygame.K_UP and not sorting:
        ascending = True
      elif event.key == pygame.K_DOWN and not sorting:
        ascending = False
      elif event.key == pygame.K_i and not sorting:
        sortingAlgorithm = insertionSort
        _sortingAlgorythm = "Insertion Sort"
      elif event.key == pygame.K_b and not sorting:
        sortingAlgorithm = bubbleSort
        _sortingAlgorythm = "Bubble Sort"
        
  pygame.quit()

main()
