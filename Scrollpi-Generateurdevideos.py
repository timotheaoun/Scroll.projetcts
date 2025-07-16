#Générateur de vidéo pour un scroll sur les décimales de pi
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1080, 1920
FRAMES = 18000
FPS = 30
DIGITS_PER_LINE = 40
LINE_HEIGHT = 40
LINES_PER_FRAME = HEIGHT // LINE_HEIGHT
DIGIT_HEIGHT = LINE_HEIGHT
SCROLL_SPEED = 3

base_pi = (
    "141592653589793238462643383279502884197169399375105820974944592307816406286"
    "208998628034825342117067982148086513282306647093844609550582231725359408128"
)
pi_digits = (base_pi * 20000)[:FRAMES * SCROLL_SPEED * DIGITS_PER_LINE]

def get_color(digit):
    base = [160, 196, 255]
    dark = [0, 40, 90]
    ratio = int(digit) / 9
    r = round(base[0] + ratio * (dark[0] - base[0]))
    g = round(base[1] + ratio * (dark[1] - base[1]))
    b = round(base[2] + ratio * (dark[2] - base[2]))
    return (r, g, b)

os.makedirs("frames", exist_ok=True)

try:
    font = ImageFont.truetype("DejaVuSansMono.ttf", 30)
except:
    font = ImageFont.load_default()

for frame in range(FRAMES):
    img = Image.new("RGB", (WIDTH, HEIGHT), (240, 240, 240))
    draw = ImageDraw.Draw(img)
    start_line = frame * SCROLL_SPEED
    for i in range(LINES_PER_FRAME):
        offset = (start_line + i) * DIGITS_PER_LINE
        line_digits = pi_digits[offset:offset + DIGITS_PER_LINE]
        for j, digit in enumerate(line_digits):
            x = j * (WIDTH // DIGITS_PER_LINE)
            y = i * LINE_HEIGHT
            color = get_color(digit)
            draw.text((x, y), digit, font=font, fill=color)
    img.save(f"frames/frame_{frame:05d}.png")
    print(f"{frame+1}/{FRAMES}", end='\r')

print()
