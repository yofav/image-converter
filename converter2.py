from PIL import Image, ImageFilter, ImageOps
import os, sys 
from time import sleep
import random

#first function
def first():
    print("\n\037This is the best image converter you will use!!]\n")
    print("\033[1;22mImage 1 : Seal\n")
    print("\033[1;24mImage 2 : Goat\n")
    print("\033[1;26mImage 3 : Panda\n")
    print("\033[1;28mImage 4 : Dino\n")
    print("\033[1;29mImage 5 : Dog\n ")
    print("\033[1;30mImage 6 : Puppy\n ")
    print("\033[1;32mImage 7 : Ape\n ")
    print("\033[1;34mImage 8 : Goose\n ")
    print("\033[1;36mImage 9 : Moose\n ")
    print("\033[1;38mImage 10 : Bird\n ")
    print("\033[1;34mWhich image would you like to pick from 1-10, if you want to quit press q")

    answer = input("")
    
    if answer == "q":
        quit()
        
    if answer == "1":
            Image = Image.open("1.jpg")
    elif answer == "2":
            Image = Image.open("2.jpg")
    elif answer == "3":
            Image = Image.open("3.jpg")
    elif answer == "4":
            Image = Image.open("4.jpg")
    elif answer == "5":
            Image = Image.open("5.jpg")
    elif answer == "6":
            Image = Image.open("6.jpg")
    elif answer == "7":
            Image = Image.open("7.jpg")
    elif answer == "8":
            Image = Image.open("8.jpg")
    elif answer == "9":
            Image = Image.open("9.jpg")
    elif answer == "10":
            Image = Image.open("10.jpg")
    else:
            answer = random.randint(1, 10)
            Image = Image.open(f"{answer}.jpg")
            Image.show()

    sleep(1.0)
    os.system('cls')


    def change():
            
            print('\033[1;33mIf you want to convert the image from " jpg" to " png", press 1\n"')
            print('\033[1;36mIf you want to change the thumbnail size of the image, press 2\n"')
            print('\033[1;31mIf you want to change the rotation of the image, press 3\n"')
            print('\033[1;35mIf you want to make the image black & white, press 4\n"')
            print("\033[1;32mIf you want to blur the image, press 5\n")
            print('\033[1;33mIf you want to add a border to your image, press 6\n"')
            print('\033[1;31mPress "Q" to quitin')
            
            #clear term
            change = input(""). lower()
            sleep(1.5)
            os.system("cls")
            if change == "1":
              png_filename = input('\033[1:35mPut down a name for the brand new png file:  ')
      
      
            code_dir = os.path.dirname(os.path.abspath(__file__))

        # create png
            Png_dir = os.path. join(code_dir, "png pics")
            if not os.path.exists(Png_dir):
                os.mkdir(Png_dir)

            thumb_filepath = os.path. join(Png_dir, png_file + " png")


            while os.path.exists(png_filepath):
                print(f" {png_filepath} already exists.")
                png_filename = input('\033[1;34mEnter a different name for the new PNG file: ')
                png_filepath = os.path. join(Png_dir, png_filename + ".png")

            Image.save (png_filepath, format="PNG")
            print("\033[1;33mWouldyou like to view your edited file? (y/n)")
            view = input(""). lower()

            if view == "y":
                Image.show()

            elif change == "2":
            # variable that will help us determine if to run the code or not for thumbnail sizes
                valid_input = False
            while not valid_input:
                thumb_size = input("\n\033[1;34mEnter a thumbnail size (200, 400, or 600): ")
            image_filename = input(" \033[1;34mEnter a name for the new Rotated file: ")

            if thumb_size not in ["200","400","600"]:
                print('\033[1;31mInvalid input. Please enter one of the three values available ~~~ 200, 400, or 600')
            else:
                valid_input = True
            # code that will create the folders depending on size. Name will be something Like 'thumbnaiL 400*
            code_dir = os.path.dirname(os.path.abspath(__file__))
            thumb_dir = os.path.join(code_dir, f"thumbnail_{thumb_size}")

            if not os.path.exists(thumb_dir):
                os.mkdir(thumb_dir)

            thumb_filepath = os.path.join(thumb_dir, f'{image_filename}_thumb{thumb_size}.jpg')

            while os.path.exists(thumb_filepath):
                print(f'{thumb_filepath} already exists \n')
            thumb_filepath = input('\033[1;35mEnter a different name for the thumbnail file; \n')
            thumb_filepath = os.path.join(thumb_dir, thumb_filepath + ".jpj")

            Image.thumbnail((int (thumb_size), int (thumb_size)))
            Image.save(thumb_filepath, format-"JPEG")

            print('\033[1;33mWould you like to view your edited file? (y/n)')
            view = input(""). lower()
            
            if view == "v":
            # open the saved thumbnail file and display it
                img = Image.open(thumb_filepath)
                img.show()

            elif change == "3":
            
                angle = float((input('\033[1;35mWhat are you going to name your new rotated image: ')))
                rotated_filename = input('\033[1;34mWhat would you like to name your new rotated image: ')
                rotated_image = Image.rotate(angle)

                code_dir = os.path.dirname(os.path.abspath(__file__))
                rotated_dir = os.path. join(code_dir, "rotated") 
            
            if not os.path.exists(rotated_dir):
                os.mkdir(rotated_dir)

                rotated_filepath = os.path. join(rotated_dir, rotated_filename + ".jpg")

            while os.path.exists(rotated_filepath):
                print(f"{rotated_filepath} already exists \n")
                rotated_filename = input ('\033[1;34mEnter a different name for the new Rotated file: \n')
                rotated_filepath = os.path. join(rotated_dir, rotated_filename +" jpg")

                rotated_image.save(rotated_filepath, format="JPEG")

                print(" \033[1;33mWould you like to view your edited file? (y/n)")
                view = input("").lower()

            if view == "y":
                img = Image.open(rotated_filepath)
                img.show

            elif change == "4":
            # coverting for black and white
                bw_image = Image.convert("")
            
                bw_filename = input('\033[1;34mEnter a name for the black and white image:')

                code_dir = os.path.dirname(os.path.abspath(__file__))

                bw_dir = os.path. join(code_dir, "black-white")
            if not os.path.exists(bw_dir):
                os.mkdir(bw_dir)

                bw_filepath = os.path. join(bw_dir, bw_filename + " jpg")

            while os.path.exists(bw_filepath):
                print(f" bw filepath already exists\n")
                bw_filename = input('\033[1;34mEnter a different name for the new Black & White file: In')
                bw_filepath = os.path.join(bw_dir, bw_filename +".jpg")

                bw_image.save(bw_filepath, format="JPEG")

                print("\033[1;33mWould you like to view your edited file? (y/n)")
                view = input("").lower()

            if view == "y":
            # open the saved bw file and display 
                img = Image.open(bw_filepath)
                img.show()

            elif change == "5":
                blur_radius = int(input("\033[1;34mEnter a blur radius : ")) 
                blurred_image = Image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

                blur_filename = input("\033[1;34mEnter a name for the blurred image: ")

                code_dir = os.path.dirname(os.path.abspath( __file__ ))

                blur_dir = os.path.join(code_dir, "blurred")
            if not os.path.exists(blur_dir):
                os.mkdir(blur_dir)

                blur_filepath = os.path.join(blur_dir, blur_filename + " jpg")


            while os.path.exists(blur_filepath):
                print(f"(blur_filepath) already exists\n")
                blur_filename = input(" \033[1;34mEnter a different name for the new Blurred file: In")
                blur_filepath = os.path.join(blur_dir, blur_filename + " jpg")

                blurred_image.save(blur_filepath, format="JPEG")

                print(" \033[1;33mwould you like to view your edited file? (y/n)")
                view = input(""). lower()

            if view == "y":
            # the saved blur file and display
                img = Image.open(blur_filepath)
                img.show()
            elif change == "6":
                valid_input = False
            while not valid_input:
                print('\033[1;34mEnter a number between 1 - 10. If your number does not meet the range of numbers, the border will be set to 5 as default: ')
                border = input(""). lower()
            if border.isdigit() and int(border) in range(1, 11):
                border = int(border)
                valid_input = True
            else:
                border = 5
                valid_input = True
            
                valid_color = False

            while not valid_color:
                print('\033[1;34mEnter a border color from the following --- red, black, or yellow: ')
                color = input(""). lower()

            if color in ["red", "black", "yellow"]:
                valid_color = True

            else:
                color = "black"
                valid_color = True


                border_filename = input(' \033[1;34mEnter a name for the bordered image: ')

                code_dir = os.path. dirname (os.path.abspath(__file__))

                border_dir = os.path.join(code_dir, "Bordered")
            if not os.path.exists(border_dir):
                os.makedirs (border_dir)
                border_filepath = os.path.join(border_dir, border_filename +".jpg")

            while os.path.exists (border_filepath):
                print(f" {border_filepath} already exists \n",)
                border_filename = input ("\033[1;34mEnter a different name for the new Bordered file: In")
                border_filepath = os.path.join(border_dir, border_filename +" jpg")

                bordered_image = ImageOps.expand (Image, border-border, fill=color)
                bordered_image.save (border_filepath, format-"JPEG")

                print(" \033[1;33mwould you like to view your edited file? (y/n)")
                view = input == "y"

            if view == "y": #open
                img = Image.open(border_filepath)
                img.show()

            elif change =="q":
                print("\033[1;32mSee you Later!")
                quit()

            else:
                print('\033[1;31mYou provided an invalid value. Please pick a number from 1 - 6 or press "q to quit\n')
                change()

                sleep(1.5)
                os.system("cls") #clears the terminal

                print("\033[1;32 would you like to keep working with Image Manipulator? (y/n)in")
                end = input ("").lower()

                sleep(1.5)
                os.system("cls") #clears the terminal
            if end == "y":
                print('\033[1;32mrun it back fam...')
                sleep(1.5)
                os.system("cls")
                first()
            else:
                print("\033[1;32mYoure done")
                quit()

first() 