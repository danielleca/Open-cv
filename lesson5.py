import os, cv2
from PIL import Image

path = r"/Users/daniellecampbell/Desktop/Coding/Open CV/images"

os.chdir(path)
mean_height = 0
mean_width = 0

image_files = []

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        image_files.append(file)

num_of_images = len(image_files)

for file in  image_files:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width += width
    mean_height += height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images
print("Average Width: ", mean_width)
print("Average Height: ", mean_height)

for file in image_files:
    img = Image.open(os.path.join(path,file))
    width, height = img.size
    print(width, height)
    imgResized = img.resize((mean_width, mean_height), Image.LANCZOS)
    imgResized.save(file, 'JPEG', quality = 95)
    print(file, "is resized")


video_name = "MyFirstVideo.avi"
frame = cv2.imread(image_files[0]) 
height, width, layers = frame.shape 

fourcc = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

for image in image_files:
    frame = cv2.imread(image)
    video.write(frame)

video.release()
cv2.destroyAllWindows()
print("Video Created Successfully")

cap = cv2.VideoCapture(video_name)
while True:
    ret, frame=cap.read()

    if not ret:
        break

    cv2.imshow("Video slideshow", frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()