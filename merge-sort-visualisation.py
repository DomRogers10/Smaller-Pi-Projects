import pygame
import time
import random

pygame.init()

window = pygame.display.set_mode((640, 500))

pygame.display.flip()
def divide(lst, depth, start_index):
    if len(lst) == 1 or len(lst) == 2:
        for i in range(len(lst)):
            height = int(f"{(330 * (lst[i] / divider)):.0f}")
            print(pygame.draw.rect(window, (255, 0, 0), pygame.Rect(20 + ((start_index + i) * 6), 370-height, 5, height)))
        lst.sort()
        for i in range(len(lst)):
          height = int(f"{(330 * (lst[i] / divider)):.0f}")
          print(pygame.draw.rect(window, (0, 0, 0), pygame.Rect(20 + ((start_index + i) * 6), 0, 5, 370)))
          time.sleep(0.05)
          print(pygame.draw.rect(window, (255, 255, 255), pygame.Rect(20 + ((start_index + i) * 6), 370-height, 5, height)))
          pygame.display.flip()
          time.sleep(0.05)
        return [lst]
    else:
        split = []
        split = split + divide(lst[:len(lst) // 2], depth + 1, start_index)
        split = split + divide(lst[len(lst) // 2:], depth + 1, start_index + (len(lst) // 2))
        return merge(split[0], split[1], start_index)
    


def merge(lst, lsts, start_index):
    z = []
    index = 0
    indexs = 0
    lstss = lst + lsts
    for i in range(len(lstss)):
      height = int(f"{(330 * (lstss[i] / divider)):.0f}")
      print(pygame.draw.rect(window, (255, 0, 0), pygame.Rect(20 + ((start_index + i) * 6), 370-height, 5, height)))
    while True:
        if index >= len(lst):
            for i in range(indexs, len(lsts)):
                z.append(lsts[i])
            break
        elif indexs >= len(lsts):
            for i in range(index, len(lst)):
                z.append(lst[i])
            break
        if index >= len(lst) and indexs >= len(lsts):
            break
        if lst[index] <= lsts[indexs]:
            z.append(lst[index])
            index += 1
        else:
            z.append(lsts[indexs])
            indexs += 1
    for i in range(len(z)):
      height = int(f"{(330 * (z[i] / divider)):.0f}")
      print(pygame.draw.rect(window, (0, 0, 0), pygame.Rect(20 + ((start_index + i) * 6), 0, 5, 370)))
      time.sleep(0.05)
      print(pygame.draw.rect(window, (255, 255, 255), pygame.Rect(20 + ((start_index + i) * 6), 370-height, 5, height)))
      pygame.display.flip()
      time.sleep(0.05)
    return [z]

lst = [i for i in range(1, 101)]
random.shuffle(lst)
divider = max(lst)
for i in range(len(lst)):
  height = int(f"{(330 * (lst[i] / divider)):.0f}")
  print(pygame.draw.rect(window, (255, 255, 255), pygame.Rect(20 + (i * 6), 370-height, 5, height)))
  pygame.display.flip()
lst = divide(lst, 0, 0)[0]
