import io
import os
import types
from PIL import Image, ImageDraw
# import all apis needed:
from google.cloud import vision
from google.cloud import storage

# from google.cloud.vision import types

# instantiate a vision annotator
client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://bucket-67/subj0.jpg'

# instantiate a storage client
# storclient = storage.Client()
# get bucket
# bucket = client.get_bucket('bucket-67')
response = client.text_detection(image=image)
#document_text_detection was more effective
#response1 = client.document_text_detection(image=image)
texts = response.text_annotations
print('Texts:')
# print(texts)

for text in texts:
    print(text.description)
    # print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))

# test annotator
# response = client.annotate_image({
#    'image': {'source': {'image_uri': 'gs://bucket-67/subj1.jpg'}},
#    'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],

# })
# len(response.annotations)

# for text in response.annotations[0]:
#    print(text)
