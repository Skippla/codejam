import json
from watson_developer_cloud import VisualRecognitionV3

test_url = 'http://www.veronapizza.co.uk/wp-content/uploads/2017/01/pizza_trad_pepperoni.png'
visual_recognition = VisualRecognitionV3('2017-08-09', api_key='4f3cb412fddb93a43ee758b0f4b9704c15d50aa8')

url_result = visual_recognition.classify(images_url=test_url)
print(json.dumps(url_result, indent=2))

