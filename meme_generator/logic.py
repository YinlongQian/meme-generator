from flickrapi import FlickrAPI

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