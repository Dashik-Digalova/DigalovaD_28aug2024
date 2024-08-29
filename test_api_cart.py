import requests
import allure


@allure.title("Check empty cart")
def test_get_cart_contents(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get('https://web-gate.chitai-gorod.ru/api/v1/cart', headers=headers)
    assert response.status_code == 200


@allure.title("add product")
def test_add_product_to_cart(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"id":3019496,"adData":{"item_list_name":"cart","product_shelf":"Просмотренные товары"}}
    response = requests.post("https://web-gate.chitai-gorod.ru/api/v1/cart/product", json=payload, headers=headers)
    assert response.status_code == 200


@allure.title("Delete product from cart")
def test_delete_product_from_cart(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.delete("https://web-gate.chitai-gorod.ru/api/v1/cart", headers=headers)
    assert response.status_code == 204

