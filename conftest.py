import pytest

from Services.entity_request import EntityRequest
from Entity.entity_model import Entity
from Services.data_generator import Generator

@pytest.fixture
def entity_api() -> EntityRequest:
    return EntityRequest

@pytest.fixture
def entitymodel() -> Entity:
    return Entity

@pytest.fixture()
def generate_data() -> Generator.generate_client_data:
    return Generator.generate_client_data