import numpy as np
from PIL import Image 

im = Image.open("./ascii-pineapple.jpg")
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




def try1(imagearray):
	imagelist = []
	for i in image_array:
		sum_of_tuple=0
		
		for j in i:
			sum_of_tuple += j

		average = int(sum_of_tuple/3)
		imagelist.append(average)
	
	return imagelist

#rename this stuff
test2 = try1(image_array)


brightness_ch = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"



# def convert_bri_to_asc(bri, asc):
# 	listofascii = []
# 	asc_ch = ""
# 	# if bri < 5:
# 	# 	asc_ch = ""
# 	for i in bri:
# 		percent_num = bri[i]/256
# 		asc_perc = int(len(asc) * percent_num)
		
# 		asc_ch = asc[asc_perc]
# 		listofascii.append(asc_ch)

# 	finallist = (''.join(listofascii))
# 	return finallist

# #test3 = convert_bri_to_asc(test2, brightness_ch)




	#now for the first numbers like 0 etc. because they give 0 and the index is -1
#elle = [232,123,55,1,255,164]

def convert_bri_to_asc2(brightness, characters):
	listofascii = []
	asc_ch = ""
	# if bri < 5:
	# 	asc_ch = ""
	# for i in brightness:

	for i in brightness:
		percent_num = i/256
		asc_perc = int(len(characters) * percent_num)
		
			
		asc_ch = characters[asc_perc]
		
		listofascii.append(asc_ch)

	finallist = (''.join(listofascii))
	return finallist



test4 = convert_bri_to_asc2(test2, brightness_ch)


# convert brightness numbers to ascii characters depending on position etc. 
# I have this list of "x" characters 
# I have a list of averages from 0-255 
# 1. Create a spectrum (len(ch)/255) = x (sowas kommt dann ca raus)
# 2. Dann muss ich die "ch" liste teilen in "x" 


			


if __name__ == "__main__":
	# print(brightness_ch)
	# print(len(brightness_ch))
	# print(brightness_ch[int(len(brightness_ch))-1])
	# print(test2)
	print("Hi")
	print(len(test2))
	print(test4)