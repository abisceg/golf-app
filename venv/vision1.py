import io
import os
import types
# from PIL import Image, ImageDraw
# import all apis needed:
from google.cloud import vision
from google.cloud import storage

# from google.cloud.vision import types

# instantiate a vision annotator
client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://bucket-67/oldwayland1.jpg'
# get a response
response = client.text_detection(image=image)
# text_detection was more effective
# response1 = client.document_text_detection(image=image)
texts = response.text_annotations

def PrettyView(texts):
    result = []
    result1 = []
    for text in texts:
        #print(text.description)
	result.append(text.description)
        # print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        result1.append('bounds: {}'.format(','.join(vertices)))
       #print('bounds: {}'.format(','.join(vertices)))
    return result


view1 = PrettyView(texts)
print(view1)



#for i in view1:
#    print(i)


#print(view1)


# test annotator
# response = client.annotate_image({
#    'image': {'source': {'image_uri': 'gs://bucket-67/subj1.jpg'}},
#    'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],

# })
# len(response.annotations)

# for text in response.annotations[0]:
#    print(text)
