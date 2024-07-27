mock_accounts = [
    {
        "user_id": 0,
        "username": 'admin',
        "password": 'pass',
       	"first_name": 'admin',
        "last_name": 'admin',
        "current_transaction": [],
        "admin": True
    },
    {
        "user_id": 1,
        "username": 'bthiele',
        "password": 'pass',
        "first_name": 'Ben',
        "last_name": 'Thiele',
        "current_transaction": [{"item_id": 0, "quantity": 4}, {"item_id": 4, "quantity": 10}],
        "admin": False
    },
    {
        "user_id": 2,
        "username": 'jheld',
        "password": 'pass',
        "first_name": 'James',
        "last_name": 'Held',
        "current_transaction": [{"item_id": 1, "quantity": 15}],
        "admin": False
    },
    {
        "user_id": 3,
        "username": 'lShields',
        "password": 'pass',
        "first_name": 'Lex',
        "last_name": 'Shields',
        "current_transaction": [{"item_id": 0, "quantity": 4}, {"item_id": 4, "quantity": 13}, {"item_id": 2, "quantity": 5}, {"item_id": 1, "quantity": 8}],
        "admin": False
    },
    {
        "user_id": 4,
        "username": 'tJohnson',
        "password": 'pass',
        "first_name": 'Terry',
        "last_name": 'Johnson',
        "current_transaction": [{"item_id": 3, "quantity": 7}, {"item_id": 4, "quantity": 20}],
        "admin": False
    }
]

mock_items = [
    {
        "item_id": 0,
        "item_name": 'Banana',
        "price": 0.99,
        "current_inventory": 10
    },
        {
        "item_id": 1,
        "item_name": 'Apple',
        "price": 1.27,
        "current_inventory": 10
    },
    {
        "item_id": 2,
        "item_name": 'Tomato',
        "price": 2.13,
        "current_inventory": 10
    },    
    {
        "item_id": 3,
        "item_name": 'Cabbage',
        "price": 0.29,
        "current_inventory": 10
    },    
    {
        "item_id": 4,
        "item_name": 'Chicken',
        "price": 2.99,
        "current_inventory": 10
    }
]

mock_transaction = {
  "transaction_id": 1,
  "user_id": 2,
  "date": "2024-07-27T03:00:07.920929",
  "items": [
    {
      "item_id": 1,
      "quantity": 15
    }
  ],
  "total_cost": 19.05
}