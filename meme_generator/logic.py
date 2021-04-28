from flickrapi import FlickrAPI
from PIL import Image, ImageDraw, ImageFont
import requests

KEY = '4546161ab5017be8109ad0dd344b8889'
SECRET = '18a350469e886e62'
SIZES = ['url_l', 'url_c', 'url_z', 'url_m', 'url_n']

def search_images(search_keyword):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    images = flickr.walk(text=search_keyword,
                         extras=extras,
                         sort='relevance')
    return images

def extract_urls(images):
    image_count = 0
    image_urls = []
    for image in images:
        if image_count >= 15:
            break
            
        for size in SIZES:
            image_url = image.get(size)
            if image_url:
                image_urls.append(image_url)
                image_count += 1
                break
                
    return image_urls

def download_image(image_url, image_dir):
    response = requests.get(image_url)

    file = open(image_dir, "wb")
    file.write(response.content)
    file.close()

def generate_meme(image_dir, meme_text, meme_dir):
    meme_back = Image.open(image_dir)
    back_w, back_h = meme_back.size

    meme_img = Image.new('RGBA', (back_w, back_h+100), (255,255,255,255))
    draw = ImageDraw.Draw(meme_img)

    font = ImageFont.truetype("arial.ttf", 80)
    text_w, text_h = draw.textsize(meme_text, font=font)

    draw.text(((back_w - text_w)//2,back_h+10), meme_text, (0,0,0), font=font)
    meme_img.paste(meme_back, (0,0))
    meme_img.save("static/" + meme_dir)