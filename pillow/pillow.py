from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import base64

if __name__ == '__main__':
    with Image.open('mug.png').convert("RGBA") as im:
        txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
        fnt = ImageFont.load_default(50)
        d = ImageDraw.Draw(txt)
        # draw text, half opacity
        d.text(((im.size[0] / 2), (im.size[1] / 2)), "Jospin", font=fnt, fill="black")

        out = Image.alpha_composite(im, txt)
        image_bytes = BytesIO()
        out.save(image_bytes, format='PNG')
        image_data = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        print(image_data)

        out.show()
