import PIL.Image
from datetime import datetime

#ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", "$"]

#resize image according to a new widht
def resize_image(image, new_width=100):
    widht, height = image.size
    ratio = height / widht
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    #attempt to open image from usr-input
    path = input("Enter a pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image")
        return

    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:(i+new_width)] 
        for i in range(0, pixel_count, new_width)
    )

    #print result
    print(ascii_image)

    #save result with date + time
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ascii_image_{now}.txt"

    with open(filename, "w") as f:
        f.write(ascii_image)

    print("Saved as", filename)

main()