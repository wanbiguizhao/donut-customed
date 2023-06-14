from PIL import Image, ImageDraw, ImageFont

# get an image
# with Image.open("dataset/font/x-1.png").convert("RGBA") as base:
#     print(base.size)
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

#     # get a font
#     fnt = ImageFont.truetype("dataset/font/思源宋体-Regular.otf", 29)
#     # get a drawing context
#     d = ImageDraw.Draw(txt) 

#     # draw text, half opacity
#     d.text((385, 232), "000202、000203", font=fnt, fill=(0, 0, 0, 255))
#     d.text((1200, 232), "京东方A、北京大发", font=fnt, fill=(0, 0, 0, 255))
#     # draw text, full opacity
#     #d.text((365, 273), "World", font=fnt, fill=(0, 0, 0, 255))
#     out = Image.alpha_composite(base, txt)
#     out.show()

def drawImage(code_text,short_name,image_save_path):
    with Image.open("dataset/font/x-1.png").convert("RGBA") as base:
        #print(base.size)
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("dataset/font/思源宋体-Regular.otf", 29)
        # get a drawing context
        d = ImageDraw.Draw(txt) 

        # draw text, half opacity
        d.text((385, 232), code_text, font=fnt, fill=(0, 0, 0, 255))
        d.text((1200, 232), short_name, font=fnt, fill=(0, 0, 0, 255))
        # draw text, full opacity
        #d.text((365, 273), "World", font=fnt, fill=(0, 0, 0, 255))
        out = Image.alpha_composite(base, txt)
        out.convert('RGB').save(image_save_path)