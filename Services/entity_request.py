from typing import List

import allure
from pydantic import ValidationError

from Entity.entity_model import Entity
from Services.request_handler import Request

request = Request()


class EntityRequest:
    @staticmethod
    @allure.step('Отправить запрос на добавление сущности')
    def create_entity(entity: Entity) -> str:
        response = request.send_request('POST', 'create', entity.model_dump_json())
        return response.json()

    @staticmethod
    @allure.step('Отправить запрос на удаление сущности')
    def delete_entity(id: int) -> None:
        request.send_request('DELETE', f'delete/{id}')

    @staticmethod
    @allure.step('Отправить запрос на получение сущности')
    def get_entity(id: int):
        response = request.send_request('GET', f'get/{id}')
        try:
            return Entity.model_validate(response.json())
        except ValidationError:
            return False

    @staticmethod
    @allure.step('Отправить запрос на получение списка всех сущностей')
    def get_all_entities() -> List[Entity]:
        response = request.send_request('GET', f'getAll')
        return [Entity.model_validate(entity) for entity in response.json()['entity']]

    @staticmethod
    @allure.step('Отправить запрос на изменение сущности')
    def patch_entity(id: int, entity: Entity):
        request.send_request('PATCH', f'patch/{id}', entity.model_dump_json())