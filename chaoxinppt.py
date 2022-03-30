from PIL import Image
from io import BytesIO
import requests

imgHref = 'https://s3.ananas.chaoxing.com/doc/31/a1/b8/e181b5a08384a9df472773b8ab672508/thumb/110.png'
imgList = []
iscontinue = True
while iscontinue:
    lastPageLink = str(input("input last png 's link:"))
    imgHref = '/'.join(lastPageLink.split('/')[:-1]) + '/'
    sumPages = int(lastPageLink.replace(imgHref,'').replace('.png','')) + 1
    name = lastPageLink.split('/')[-3]
    print('page url: {''}\nsum page(s): {:d}'.format(imgHref, sumPages-1))
    for page in range(1, sumPages):
        print('\rdownloading page: {:d} , {:d} page(s) in total'.format(page,sumPages-1), end = '')
        response = requests.get(imgHref + str(page) + '.png').content
        BytesIOObj = BytesIO()
        BytesIOObj.write(response)
        img = Image.open(BytesIOObj).convert( "RGB" )
        imgList.append(img)
    imgList[0].save("E:/"+name+".pdf", "pdf", save_all=True, append_images=imgList[1:])
    iscontinue = input("input 1 means continue, others means quit:") == '1'
