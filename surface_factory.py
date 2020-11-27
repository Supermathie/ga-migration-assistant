import pygame
import qrcode.image.base

# adapted from https://github.com/lincolnloop/python-qrcode/pull/133
class SurfaceFactory(qrcode.image.base.BaseImage):
  def new_image(self, **kwargs):
    back_color = pygame.Color(kwargs.get("back_color", "white"))
    fill_color = pygame.Color(kwargs.get("fill_color", "black"))
    self.fill_color = fill_color
    surface = pygame.Surface((self.pixel_size, self.pixel_size))
    surface.fill(back_color)
    return surface

  def drawrect(self, row, col):
    rect = pygame.Rect(self.pixel_box(row, col)[0], (self.box_size,self.box_size))
    self._img.fill(color=self.fill_color, rect=rect)
      
  def surface(self):
    return self._img
