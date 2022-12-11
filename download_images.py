from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["handgun in the hand"]

for k in keywords:
    response().download(k,100)