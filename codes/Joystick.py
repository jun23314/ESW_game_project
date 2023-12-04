from digitalio import DigitalInOut, Direction
from adafruit_rgb_display import st7789
import board

class Joystick:
    def __init__(self):
        self.cs_pin = DigitalInOut(board.CE0)
        self.dc_pin = DigitalInOut(board.D25)
        self.reset_pin = DigitalInOut(board.D24)
        self.BAUDRATE = 24000000

        self.spi = board.SPI()
        self.disp = st7789.ST7789(
                    self.spi,
                    height=240,
                    width=240,
                    y_offset=80,
                    rotation=180,
                    cs=self.cs_pin,
                    dc=self.dc_pin,
                    rst=self.reset_pin,
                    baudrate=self.BAUDRATE,
                    )

        # Input pins:
        self.button_Five = DigitalInOut(board.D5)
        self.button_Five.direction = Direction.INPUT

        self.button_Six = DigitalInOut(board.D6)
        self.button_Six.direction = Direction.INPUT

        self.button_Left = DigitalInOut(board.D27)
        self.button_Left.direction = Direction.INPUT

        self.button_Right = DigitalInOut(board.D23)
        self.button_Right.direction = Direction.INPUT

        self.button_Up = DigitalInOut(board.D17)
        self.button_Up.direction = Direction.INPUT

        self.button_Down = DigitalInOut(board.D22)
        self.button_Down.direction = Direction.INPUT

        self.button_Center = DigitalInOut(board.D4)
        self.button_Center.direction = Direction.INPUT

        # Turn on the Backlight
        self.backlight = DigitalInOut(board.D26)
        self.backlight.switch_to_output()
        self.backlight.value = True

        # Create blank image for drawing.
        # Make sure to create image with mode 'RGB' for color.
        self.width = self.disp.width
        self.height= self.disp.height
