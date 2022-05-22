from email.mime import image
from tkinter import image_names
from PIL import Image, ImageDraw

img = Image.open('./basic.png')
draw = ImageDraw.Draw(img)


type, type_unknown = 10, False
rice, rice_unknown = 78, True
shubo, shubo_unknown = 25, False
result = 46
yeast, yeast_unknown = 50, False
amino, amino_unknown = 50, False
acid, acid_unknown = 50, False
smv, smv_unknown= -4, False
body = 50
wine = 50

pic_margin = 225
pic_width = 1135

solid_color = "orange"
light_color = "lightgray"



start_x, start_y = pic_margin+(pic_width/100)*type, 10
type_x, type_y = pic_margin+(pic_width/100)*type, 72
rice_x, rice_y = pic_margin+(pic_width/100)*rice, 178
shubo_x, shubo_y = pic_margin+(pic_width/100)*shubo, 293 
result_x, result_y = pic_margin+(pic_width/100)*result, 460 


unknown = [type_unknown, rice_unknown, shubo_unknown]

dummy = 0

for unknown_value in unknown:
    if not unknown_value and dummy == 0:
        draw.line([(start_x, start_y), (type_x, type_y)], fill = solid_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 0:
        print("Hello")
        draw.line([(start_x, start_y), (type_x, type_y)], fill = light_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 1:
        if unknown[dummy-1]:
            draw.line([(type_x, type_y), (rice_x, rice_y)], fill = "lightgray", width = 8, joint="curve")
        if not unknown[dummy-1]:
            draw.line([(type_x, type_y), (type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2)], fill = solid_color, width = 8, joint="curve")
            draw.line([(type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2), (rice_x, rice_y)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 1:
        if not unknown[dummy-1]:
            draw.line([(type_x, type_y), (rice_x, rice_y)], fill = solid_color, width = 8, joint="curve")
        if unknown[dummy-1]:
            draw.line([(type_x, type_y), (type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2)], fill = light_color, width = 8, joint="curve")
            draw.line([(type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2), (rice_x, rice_y)], fill = solid_color, width = 8, joint="curve") 

    if unknown_value and dummy == 2:
        if unknown[dummy-1]:
            draw.line([(rice_x, rice_y), (shubo_x, shubo_y)], fill = "lightgray", width = 8, joint="curve")
        if not unknown[dummy-1]:
            draw.line([(rice_x, rice_y), (rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2)], fill = solid_color, width = 8, joint="curve")
            draw.line([(rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2), (shubo_x, shubo_y)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 2:
        if not unknown[dummy-1]:
            draw.line([(rice_x, rice_y), (shubo_x, shubo_y)], fill = solid_color, width = 8, joint="curve")
        if unknown[dummy-1]:
            draw.line([(rice_x, rice_y), (rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2)], fill = light_color, width = 8, joint="curve")
            draw.line([(rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2), (shubo_x, shubo_y)], fill = solid_color, width = 8, joint="curve") 




    dummy += 1

if not unknown[2]:
    draw.line([(shubo_x, shubo_y), (result_x, result_y)], fill = "Orange", width = 8, joint="curve")
else:
    draw.line([(shubo_x, shubo_y), (shubo_x+(result_x-shubo_x)/3, shubo_y+(result_y-shubo_y)/3)], fill = light_color, width = 8, joint="curve")
    draw.line([(shubo_x+(result_x-shubo_x)/3, shubo_y+(result_y-shubo_y)/3), (result_x, result_y)], fill = solid_color, width = 8, joint="curve") 


img.show()
img.save('basicwline.png')

