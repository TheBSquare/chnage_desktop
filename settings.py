from pathlib import Path

work_path = Path(__file__).parent.absolute()

images_json_path = Path(work_path, 'json', 'images.json')
update_json_path = Path(work_path, 'json', 'update_data.json')

desktop_image_path = Path(work_path, 'image', 'image.jpg')