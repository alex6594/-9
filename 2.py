import requests

import os


class YandexCLoud:

    def __init__(self, token_file: str):
        self.token = token_file

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
                }

    def file_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def file_upload(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, yd_path: str):

        file_name_ = os.path.basename(file_path)
        href_json = self.file_upload(disk_file_path=yd_path)
        href = href_json['href']
        response = requests.put(href, data=open(file_path, 'rb'))

        if response.status_code < 300:
            return f"File '{file_name_}' successfully loaded to Yandex Disc."
        else:
            return f"Error code: {response.status_code}"


if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу: \t")
    file_name = input("Введите имя файла с расширением: \t")
    path_to_file = os.path.abspath(os.path.join(path_to_file, file_name))
    token = input("Введите токен яндекса: \t")
    uploader = YandexCLoud(token)
    yd_path_to_file = input("Введите название директории на яндекс диске: \t")
    yd_path_to_file = yd_path_to_file + "/" + file_name
    print(uploader.upload(path_to_file, yd_path_to_file))
