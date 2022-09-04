from utils.Necessary import get_data_by_uuid

import requests

class ValorantApi():
    url = 'https://valorant-api.com/v1'

    @classmethod
    def get_current_client_version(cls) -> str:
        response = requests.get(f'{cls.url}/version')
        data = response.json()['data']
        return data['riotClientVersion']

    @classmethod
    def get_levelborders(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/levelborders')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_currency(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/currencies')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_missions(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/missions')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_contracts(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/contracts')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_competitivetiers(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/competitivetiers')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_competitiveseasons(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/seasons/competitive')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_agents(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/agents?isPlayableCharacter=true')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_weapons(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/weapons')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_weaponskins(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/weapons/skins')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_weaponskinchromas(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/weapons/skinchromas')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_weaponskinlevels(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/weapons/skinlevels')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_sprays(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/sprays')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_buddylevels(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/buddies/levels')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_cards(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/playercards')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_titles(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/playertitles')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_contenttiers(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/contenttiers')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_themes(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/themes')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_bundles(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/bundles')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)

    @classmethod
    def get_maps(cls, uuid:str=None):
        response = requests.get(f'{cls.url}/maps')
        data = response.json()['data']
        return get_data_by_uuid(data=data, uuid=uuid)