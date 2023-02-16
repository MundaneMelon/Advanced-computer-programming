from dessertshop import Customer

def test_customer():
    customer = Customer('Robert')

    assert customer.customer_name == 'Robert'
    assert customer.customer_id == 3748327

    customer.customer_name = 'Oscar'
    customer.customer_id = 5

    assert customer.customer_name == 'Oscar'
    assert customer.customer_id == 5
