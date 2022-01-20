import numpy as np
from PIL import Image 

im = Image.open("ascii-pineapple.jpg")

image_sequence = im.getdata()
image_array = np.array(image_sequence)



#[
#[R,R,R], [G,G,G], [B,B,B],
#[R,R,R], [G,G,G], [B,B,B],
#[R,R,R], [G,G,G], [B,B,B],
#[R,R,R], [G,G,G], [B,B,B]
#]


# def brightness_converter(image_array):
# 	for i,j in image_array:
# 		print(" "+"x"+" ")


av_list = []

def try1(imagearray):
	

	for i in image_array:
		
		sum_of_tuple=0
		for j in i:
			
			sum_of_tuple += j

		
		average = int(sum_of_tuple/3)

		
		av_list.append(average)


brightness_ch = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

asc_ch = ""

def convert_bri_to_asc(bri, asc):
	listofascii = []
	# if bri < 5:
	# 	asc_ch = ""
	for i in bri:
		percent_num = (bri/256)
		asc_perc = int(len(asc) * percent_num)
		asc_ch = asc[asc_perc]
		listofascii.append[asc_ch]

	print(listofascii)



	#now for the first numbers like 0 etc. because they give 0 and the index is -1







# convert brightness numbers to ascii characters depending on position etc. 
# I have this list of "x" characters 
# I have a list of averages from 0-255 
# 1. Create a spectrum (len(ch)/255) = x (sowas kommt dann ca raus)
# 2. Dann muss ich die "ch" liste teilen in "x" 


			


if __name__ == "__main__":
	print(brightness_ch)
	print(len(brightness_ch))
	print(brightness_ch[int(len(brightness_ch))-1])
	print(av_list)
	convert_bri_to_asc(av_list, brightness_ch)
	