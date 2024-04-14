
import string
import random
from datetime import datetime
from woocommerce import API
from ssqatest.src.helpers.config_helpers import get_api_credentials
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


def create_api_object():
    api_creds = get_api_credentials()

    wcapi = API(
        url=api_creds['base_url'],
        consumer_key=api_creds['api_key'],
        consumer_secret=api_creds['api_secret'],
        version="wc/v3"
    )

    return wcapi

def create_user():
    api_obj = create_api_object()
    user_info = generate_random_email_and_password()

    create_customer_payload = {
        "email": user_info['email'],
        "password": user_info['password']

    }
    response = api_obj.post('customers', create_customer_payload)

    assert response.status_code == 201, f"Failed to create user. Response: {response.json()}"

    return user_info

def create_coupon(coupon_code=None, length=7, expired=False):

    if expired:
        expiration_date = datetime.now().isoformat()
    else:
        expiration_date = None

    if not coupon_code:
        coupon_code = ''.join(random.choice(string.ascii_uppercase) for i in range(length))

    payload = {
            "code": coupon_code,
            "discount_type": "percent",
            "amount": "100",
            "date_expires": expiration_date
        }

    api_obj = create_api_object()
    rs_api = api_obj.post('coupons', data=payload)
    assert rs_api.status_code == 201, f'Failed creating coupon. Status code {rs_api.status_code}. ' \
                                        f'Payload: {payload}. \n' \
                                        f'Response: {rs_api.json()}'

    return coupon_code

def get_coupon_info_by_coupon_code(coupon_code):
    api_obj = create_api_object()
    params = {'code': coupon_code}
    rs_api = api_obj.get('coupons', params=params)
    assert rs_api.status_code == 200, f"Failed getting coupon by coupon code: {coupon_code}"

    return rs_api.json()

def delete_coupon_by_coupon_code(coupon_code):
    api_obj = create_api_object()
    coupon_info = get_coupon_info_by_coupon_code(coupon_code)
    coupon_id = coupon_info[0]['id']
    rs_api = api_obj.delete(f"coupons/{coupon_id}", params={"force": True})
    assert rs_api.status_code == 200, f"Failed to delete coupon via api: coupon code: {coupon_code}"

def get_random_products(qty=1, **kwargs):
    """
    Gets random products using the 'products' api.
    It calls the products api with the given parameters in **kwargs, randomly selects the given number of products
    from the response and returns it.
    List of available properties: https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties
    Example function calls:
        get_random_products(qty=1, status=private, type=variable)
        get_random_products(qty=1, downloadable=True)

    :param qty: number of products to return.
    :param kwargs:
    :return:
    """
    api_obj = create_api_object()

    kwargs['per_page'] = 100

    rs_api = api_obj.get('products', params=kwargs)
    products = rs_api.json()

    return random.sample(products, int(qty))
