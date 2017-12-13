import random
import redis

from configs import products


def main():
    r = redis.client.StrictRedis(db=0)
    r.flushdb()

    list_products = products

    random.shuffle(products)
    product_men = products[0:400]

    random.shuffle(products)
    product_brand1 = products[0:200]
    product_brand2 = products[200:400]

    random.shuffle(products)
    product_blue = products[0:100]

    pipe = r.pipeline()
    [pipe.sadd('products', x) for x in list_products]
    [pipe.sadd('products:men', x) for x in product_men]
    [pipe.sadd('products:brand1', x) for x in product_brand1]
    [pipe.sadd('products:brand2', x) for x in product_brand2]
    [pipe.sadd('products:color:blue', x) for x in product_blue]
    pipe.execute()

    print 'INTER EXAMPLE'
    print "========" * 5

    result = r.sinter(['products', 'products:men', 'products:color:blue'])
    print 'total product : %s' % len(result)
    print result

    print '\n' * 4
    print 'UNION EXAMPLE'
    print "========" * 5
    r.sunionstore('union:brand1:brand2', ['products:brand1', 'products:brand2'])
    result2 = r.sinter(['products', 'products:men', 'union:brand1:brand2', 'products:color:blue'])

    print 'total product : %s' % len(result2)
    print result2


if __name__ == '__main__':
    main()