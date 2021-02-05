def get_place_images_upload_location(image_instance, filename):
    place_id = image_instance.place_id
    return 'places/{}/'.format(place_id)
