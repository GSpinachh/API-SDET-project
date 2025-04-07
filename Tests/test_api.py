import allure
from random import choice

@allure.title('Проверить функциональность добавления сущности')
def test_create_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерация сущности'):
        entity = entitymodel(**generate_data())

    id = int(entity_api.create_entity(entity))
    in_list = entity_api.get_entity(id)

    with allure.step('Проверить, есть ли сущность в списке'):
        assert in_list, 'Сущность не была создана'

@allure.title('Проверить функциональность удаления сущности')
def test_delete_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерация сущности'):
        entity = entitymodel(**generate_data())

    id = int(entity_api.create_entity(entity))
    entity_api.delete_entity(id)

    in_list = entity_api.get_entity(id)
    with allure.step('Проверить удалилась ли сущность'):
        assert not in_list, 'Сущность не удалилась'

@allure.title('Проверить функциональность получения сущности')
def test_get_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерация сущности'):
        entity = entitymodel(**generate_data())

    id = entity_api.create_entity(entity)
    in_list = entity_api.get_entity(id)

    with allure.step('Проверить, получена ли сущность'):
        assert in_list, 'Сущность не была получена'

@allure.title('Проверить функциональность получения списка сущностей')
def test_get_entities(entity_api):
    entities = entity_api.get_all_entities()

    with allure.step('Проверить, был ли получен список сущностей'):
        assert entities != [], 'Сущность не была получена'

@allure.title('Проверить функциональность изменения сущности')
def test_patch_entity(entitymodel, entity_api, generate_data):
    with allure.step('Генерация сущности'):
        entity = entitymodel(**generate_data())

    id = choice(entity_api.get_all_entities()).id
    old_entity = entity_api.get_entity(id)

    entity_api.patch_entity(id, entity)
    new_entity = entity_api.get_entity(id)

    with allure.step('Проверить изменилась ли сущность'):
        assert new_entity.model_dump_json() != old_entity.model_dump_json(), 'Сущность не изменена'
