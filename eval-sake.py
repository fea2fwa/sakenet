from email.mime import image
from tkinter import image_names
from PIL import Image, ImageDraw

img_basic = Image.open('./basic.png')
draw_basic = ImageDraw.Draw(img_basic)

img_adv = Image.open('./full.png')
draw_adv = ImageDraw.Draw(img_adv)


type, type_unknown = 10, False
rice, rice_unknown = 78, True
shubo, shubo_unknown = 25, False
result = 46
yeast, yeast_unknown = 40, False
amino, amino_unknown = 50, True
acid, acid_unknown = 60, False
smv, smv_unknown= 20, True
body = 50
wine = 50

pic_margin = 225
pic_width = 1135

solid_color = "orange"
light_color = "gainsboro"



start_x, start_y = pic_margin+(pic_width/100)*type, 10
type_x, type_y = pic_margin+(pic_width/100)*type, 72
rice_x, rice_y = pic_margin+(pic_width/100)*rice, 178
shubo_x, shubo_y = pic_margin+(pic_width/100)*shubo, 293 
result_x, result_y = pic_margin+(pic_width/100)*result, 460 


unknown = [type_unknown, rice_unknown, shubo_unknown]

dummy = 0

for unknown_value in unknown:
    if not unknown_value and dummy == 0:
        draw_basic.line([(start_x, start_y), (type_x, type_y)], fill = solid_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 0:
        print("Hello")
        draw_basic.line([(start_x, start_y), (type_x, type_y)], fill = light_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 1:
        if unknown[dummy-1]:
            draw_basic.line([(type_x, type_y), (rice_x, rice_y)], fill = light_color, width = 8, joint="curve")
        if not unknown[dummy-1]:
            draw_basic.line([(type_x, type_y), (type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2)], fill = solid_color, width = 8, joint="curve")
            draw_basic.line([(type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2), (rice_x, rice_y)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 1:
        if not unknown[dummy-1]:
            draw_basic.line([(type_x, type_y), (rice_x, rice_y)], fill = solid_color, width = 8, joint="curve")
        if unknown[dummy-1]:
            draw_basic.line([(type_x, type_y), (type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2)], fill = light_color, width = 8, joint="curve")
            draw_basic.line([(type_x+(rice_x-type_x)/2, type_y+(rice_y-type_y)/2), (rice_x, rice_y)], fill = solid_color, width = 8, joint="curve") 

    if unknown_value and dummy == 2:
        if unknown[dummy-1]:
            draw_basic.line([(rice_x, rice_y), (shubo_x, shubo_y)], fill = light_color, width = 8, joint="curve")
        if not unknown[dummy-1]:
            draw_basic.line([(rice_x, rice_y), (rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2)], fill = solid_color, width = 8, joint="curve")
            draw_basic.line([(rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2), (shubo_x, shubo_y)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 2:
        if not unknown[dummy-1]:
            draw_basic.line([(rice_x, rice_y), (shubo_x, shubo_y)], fill = solid_color, width = 8, joint="curve")
        if unknown[dummy-1]:
            draw_basic.line([(rice_x, rice_y), (rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2)], fill = light_color, width = 8, joint="curve")
            draw_basic.line([(rice_x+(shubo_x-rice_x)/2, rice_y+(shubo_y-rice_y)/2), (shubo_x, shubo_y)], fill = solid_color, width = 8, joint="curve") 


    dummy += 1

if not unknown[2]:
    draw_basic.line([(shubo_x, shubo_y), (result_x, result_y)], fill = solid_color, width = 8, joint="curve")
else:
    draw_basic.line([(shubo_x, shubo_y), (shubo_x+(result_x-shubo_x)/3, shubo_y+(result_y-shubo_y)/3)], fill = light_color, width = 8, joint="curve")
    draw_basic.line([(shubo_x+(result_x-shubo_x)/3, shubo_y+(result_y-shubo_y)/3), (result_x, result_y)], fill = solid_color, width = 8, joint="curve") 


img_basic.show()
img_basic.save('basicwline.png')




### Advanced graph drowing

pic_margin_adv = 230
pic_width_adv = 1010

start_x_adv, start_y_adv = pic_margin_adv+(pic_width_adv/100)*type, 0
type_x_adv, type_y_adv = pic_margin_adv+(pic_width_adv/100)*type, 46
rice_x_adv, rice_y_adv = pic_margin_adv+(pic_width_adv/100)*rice, 145
shubo_x_adv, shubo_y_adv = pic_margin_adv+(pic_width_adv/100)*shubo, 245
yeast_x_adv, yeast_y_adv = pic_margin_adv+(pic_width_adv/100)*yeast, 346
result_x_adv, result_y_adv = pic_margin_adv+(pic_width_adv/100)*result, 442 
amino_x_adv, amino_y_adv = pic_margin_adv+(pic_width_adv/100)*amino, 520
acid_x_adv, acid_y_adv = pic_margin_adv+(pic_width_adv/100)*acid, 580
smv_x_adv, smv_y_adv = pic_margin_adv+(pic_width_adv/100)*smv, 642
body_x_adv, body_y_adv = pic_margin_adv+(pic_width_adv/100)*body, 750

unknown_1 = [type_unknown, rice_unknown, shubo_unknown, yeast_unknown, amino_unknown]

dummy = 0

for unknown_value in unknown_1:
    if not unknown_value and dummy == 0:
        draw_adv.line([(start_x_adv, start_y_adv), (type_x_adv, type_y_adv)], fill = solid_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 0:
        draw_adv.line([(start_x_adv, start_y_adv), (type_x_adv, type_y_adv)], fill = light_color, width = 8, joint="curve")
    
    if unknown_value and dummy == 1:
        if unknown_1[dummy-1]:
            draw_adv.line([(type_x_adv, type_y_adv), (rice_x_adv, rice_y_adv)], fill = light_color, width = 8, joint="curve")
        if not unknown_1[dummy-1]:
            draw_adv.line([(type_x_adv, type_y_adv), (type_x_adv+(rice_x_adv-type_x_adv)/2, type_y_adv+(rice_y_adv-type_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
            draw_adv.line([(type_x_adv+(rice_x_adv-type_x_adv)/2, type_y_adv+(rice_y_adv-type_y_adv)/2), (rice_x_adv, rice_y_adv)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 1:
        if not unknown_1[dummy-1]:
            draw_adv.line([(type_x_adv, type_y_adv), (rice_x_adv, rice_y_adv)], fill = solid_color, width = 8, joint="curve")
        if unknown_1[dummy-1]:
            draw_adv.line([(type_x_adv, type_y_adv), (type_x_adv+(rice_x_adv-type_x_adv)/2, type_y_adv+(rice_y_adv-type_y_adv)/2)], fill = light_color, width = 8, joint="curve")
            draw_adv.line([(type_x_adv+(rice_x_adv-type_x_adv)/2, type_y_adv+(rice_y_adv-type_y_adv)/2), (rice_x_adv, rice_y_adv)], fill = solid_color, width = 8, joint="curve") 

    if unknown_value and dummy == 2:
        if unknown_1[dummy-1]:
            draw_adv.line([(rice_x_adv, rice_y_adv), (shubo_x_adv, shubo_y_adv)], fill = light_color, width = 8, joint="curve")
        if not unknown_1[dummy-1]:
            draw_adv.line([(rice_x_adv, rice_y_adv), (rice_x_adv+(shubo_x_adv-rice_x_adv)/2, rice_y_adv+(shubo_y_adv-rice_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
            draw_adv.line([(rice_x_adv+(shubo_x_adv-rice_x_adv)/2, rice_y_adv+(shubo_y_adv-rice_y_adv)/2), (shubo_x_adv, shubo_y_adv)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 2:
        if not unknown_1[dummy-1]:
            draw_adv.line([(rice_x_adv, rice_y_adv), (shubo_x_adv, shubo_y_adv)], fill = solid_color, width = 8, joint="curve")
        if unknown_1[dummy-1]:
            draw_adv.line([(rice_x_adv, rice_y_adv), (rice_x_adv+(shubo_x_adv-rice_x_adv)/2, rice_y_adv+(shubo_y_adv-rice_y_adv)/2)], fill = light_color, width = 8, joint="curve")
            draw_adv.line([(rice_x_adv+(shubo_x_adv-rice_x_adv)/2, rice_y_adv+(shubo_y_adv-rice_y_adv)/2), (shubo_x_adv, shubo_y_adv)], fill = solid_color, width = 8, joint="curve") 

    if unknown_value and dummy == 3:
        if unknown_1[dummy-1]:
            draw_adv.line([(shubo_x_adv, shubo_y_adv), (yeast_x_adv, yeast_y_adv)], fill = light_color, width = 8, joint="curve")
        if not unknown_1[dummy-1]:
            draw_adv.line([(shubo_x_adv, shubo_y_adv), (shubo_x_adv+(yeast_x_adv-shubo_x_adv)/2, shubo_y_adv+(yeast_y_adv-shubo_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
            draw_adv.line([(shubo_x_adv+(yeast_x_adv-shubo_x_adv)/2, shubo_y_adv+(yeast_y_adv-shubo_y_adv)/2), (yeast_x_adv, yeast_y_adv)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 3:
        if not unknown_1[dummy-1]:
            draw_adv.line([(shubo_x_adv, shubo_y_adv), (yeast_x_adv, yeast_y_adv)], fill = solid_color, width = 8, joint="curve")
        if unknown_1[dummy-1]:
            draw_adv.line([(shubo_x_adv, shubo_y_adv), (shubo_x_adv+(yeast_x_adv-shubo_x_adv)/2, shubo_y_adv+(yeast_y_adv-shubo_y_adv)/2)], fill = light_color, width = 8, joint="curve")
            draw_adv.line([(shubo_x_adv+(yeast_x_adv-shubo_x_adv)/2, shubo_y_adv+(yeast_y_adv-shubo_y_adv)/2), (yeast_x_adv, yeast_y_adv)], fill = solid_color, width = 8, joint="curve")


    dummy += 1

### draw result　(fruit or rice)

if not unknown_1[2]:
    draw_adv.line([(yeast_x_adv, yeast_y_adv), (result_x_adv, result_y_adv)], fill = solid_color, width = 8, joint="curve")
else:
    draw_adv.line([(yeast_x_adv, yeast_y_adv), (yeast_x_adv+(result_x_adv-yeast_x_adv)/2, yeast_y_adv+(result_y_adv-yeast_y_adv)/2)], fill = light_color, width = 8, joint="curve")
    draw_adv.line([(yeast_x_adv+(result_x_adv-yeast_x_adv)/2, yeast_y_adv+(result_y_adv-yeast_y_adv)/2), (result_x_adv, result_y_adv)], fill = solid_color, width = 8, joint="curve") 


### start dwowing again from result

if not unknown_1[4]:
    draw_adv.line([(result_x_adv, result_y_adv), (amino_x_adv, amino_y_adv)], fill = solid_color, width = 8, joint="curve")
else:
    draw_adv.line([(result_x_adv, result_y_adv), (result_x_adv+(amino_x_adv-result_x_adv)/2, result_y_adv+(amino_y_adv-result_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
    draw_adv.line([(result_x_adv+(amino_x_adv-result_x_adv)/2, result_y_adv+(amino_y_adv-result_y_adv)/2), (amino_x_adv, amino_y_adv)], fill = light_color, width = 8, joint="curve") 


unknown_2 = [acid_unknown, smv_unknown]

dummy = 0

for unknown_value in unknown_2:
    if unknown_value and dummy == 0:
        if unknown_1[-1]:
            draw_adv.line([(amino_x_adv, amino_y_adv), (acid_x_adv, acid_y_adv)], fill = light_color, width = 8, joint="curve")
        if not unknown_1[-1]:
            draw_adv.line([(amino_x_adv, amino_y_adv), (amino_x_adv+(acid_x_adv-amino_x_adv)/2, amino_y_adv+(acid_y_adv-amino_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
            draw_adv.line([(amino_x_adv+(acid_x_adv-amino_x_adv)/2, amino_y_adv+(acid_y_adv-amino_y_adv)/2), (acid_x_adv, acid_y_adv)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 0:
        if not unknown_1[-1]:
            draw_adv.line([(amino_x_adv, amino_y_adv), (acid_x_adv, acid_y_adv)], fill = solid_color, width = 8, joint="curve")
        if unknown_1[-1]:
            draw_adv.line([(amino_x_adv, amino_y_adv), (amino_x_adv+(acid_x_adv-amino_x_adv)/2, amino_y_adv+(acid_y_adv-amino_y_adv)/2)], fill = light_color, width = 8, joint="curve")
            draw_adv.line([(amino_x_adv+(acid_x_adv-amino_x_adv)/2, amino_y_adv+(acid_y_adv-amino_y_adv)/2), (acid_x_adv, acid_y_adv)], fill = solid_color, width = 8, joint="curve") 
   


    if unknown_value and dummy == 1:
        if unknown_2[dummy-1]:
            draw_adv.line([(acid_x_adv, acid_y_adv), (smv_x_adv, smv_y_adv)], fill = light_color, width = 8, joint="curve")
        if not unknown_2[dummy-1]:
            draw_adv.line([(acid_x_adv, acid_y_adv), (acid_x_adv+(smv_x_adv-acid_x_adv)/2, acid_y_adv+(smv_y_adv-acid_y_adv)/2)], fill = solid_color, width = 8, joint="curve")
            draw_adv.line([(acid_x_adv+(smv_x_adv-acid_x_adv)/2, acid_y_adv+(smv_y_adv-acid_y_adv)/2), (smv_x_adv, smv_y_adv)], fill = light_color, width = 8, joint="curve") 

    if not unknown_value and dummy == 1:
        if not unknown_2[dummy-1]:
            draw_adv.line([(acid_x_adv, acid_y_adv), (smv_x_adv, smv_y_adv)], fill = solid_color, width = 8, joint="curve")
        if unknown_2[dummy-1]:
            draw_adv.line([(acid_x_adv, acid_y_adv), (acid_x_adv+(smv_x_adv-acid_x_adv)/2, acid_y_adv+(smv_y_adv-acid_y_adv)/2)], fill = light_color, width = 8, joint="curve")
            draw_adv.line([(acid_x_adv+(smv_x_adv-acid_x_adv)/2, acid_y_adv+(smv_y_adv-type_y_adv)/2), (smv_x_adv, smv_y_adv)], fill = solid_color, width = 8, joint="curve") 

    dummy += 1


### draw body　(full or light)

if not unknown_2[1]:
    draw_adv.line([(smv_x_adv, smv_y_adv), (body_x_adv, body_y_adv)], fill = solid_color, width = 8, joint="curve")
else:
    draw_adv.line([(smv_x_adv, smv_y_adv), (smv_x_adv+(body_x_adv-smv_x_adv)/3, smv_y_adv+(body_y_adv-smv_y_adv)/3)], fill = light_color, width = 8, joint="curve")
    draw_adv.line([(smv_x_adv+(body_x_adv-smv_x_adv)/3, smv_y_adv+(body_y_adv-smv_y_adv)/3), (body_x_adv, body_y_adv)], fill = solid_color, width = 8, joint="curve") 


img_adv.show()
img_adv.save('advwline.png')