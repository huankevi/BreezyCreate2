import boto3

IMG_FILENAME = "./image.jpg"
reko_client = boto3.client('rekognition')

def find_nose_position(all_face_data, name):
    for face_data in all_face_data:
        if face_data['Name'] == name:
            for landmark in face_data['Face']['Landmarks']:
                if landmark['Type'] == "nose":
                    return landmark
    # If given name was not found return None
    return None

def yo():
    #location = 0
    image_data = open(IMG_FILENAME, 'rb')
    print("Image taken, sending it to Rekognition now")
    resp = reko_client.recognize_celebrities(Image={'Bytes' : image_data.read()})
    jassy_nose = find_nose_position(resp['CelebrityFaces'],"Andy Jassy")
    print('location is', jassy_nose)

yo()
