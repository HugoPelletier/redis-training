import redis


def main():
    r = redis.client.StrictRedis(db=0)
    r.flushdb()

    r.sadd('products', 'product:12345678')
    r.sadd('products', 'product:22287343')
    r.sadd('products', 'product:3333849')


    r.hmset('product:12345678', {
        'title': 'This is the title of product 12345678',
        'regular_price_ca': '1235',
        'sale_price_ca': '1000',
        'position': "450"
    })

    r.hmset('product:22287343', {
        'title': 'This is the title of product 22287343',
        'regular_price_ca': '1500',
        'sale_price_ca': '1200',
        'position': "90"
    })

    r.hmset('product:3333849', {
        'title': 'This is the title of product 3333849',
        'regular_price_ca': '100',
        'sale_price_ca': '10',
        'position': "3500"
    })

    print r.sort('products', by='*->position', start=0, num=1)


if __name__ == '__main__':
    main()