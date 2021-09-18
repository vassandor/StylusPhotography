def create_photo_list(number):
    photo_list = []
    for i in range(number):
        photo_list.append({
            "title": "Photo Title",
            "date": "2021.09.19.",
            "image": f"https://source.unsplash.com/400x300/?gaming,laptop{i}"
        })
    return photo_list

if __name__ == '__main__':
    photo_list = create_photo_list(10)
    pass