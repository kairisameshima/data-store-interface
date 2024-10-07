from data_store import DataStore


def test__data_store_instantiates():
    data_store = DataStore()
    assert data_store.data == {}
    assert data_store.uncommited_data == {}


def test__data_store_set():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    assert data_store.data == {"key": "value", "key2": "value2"}


def test__data_store_get():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    assert data_store.get("key") == "value"
    assert data_store.get("key2") == "value2"


def test__data_store_delete():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    data_store.delete("key")

    assert data_store.data == {"key2": "value2"}


def test__data_store_begin():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    data_store.begin()
    data_store.set("key", "value3")
    data_store.set("key2", "value4")

    assert data_store.data == {"key": "value", "key2": "value2"}
    assert data_store.uncommited_data == {"key": "value3", "key2": "value4"}

def test__data_store_commit():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    data_store.begin()
    data_store.set("key", "value3")
    data_store.set("key2", "value4")

    data_store.commit()

    assert data_store.data == {"key": "value3", "key2": "value4"}
    assert data_store.uncommited_data == {}


def test__data_store_rollback():
    data_store = DataStore()
    data_store.set("key", "value")
    data_store.set("key2", "value2")

    data_store.begin()
    data_store.set("key", "value3")
    data_store.set("key2", "value4")
    
    data_store.rollback()

    assert data_store.data == {"key": "value", "key2": "value2"}
    assert data_store.uncommited_data == {}
