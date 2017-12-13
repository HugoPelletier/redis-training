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
    product_women = products[0:600]

    random.shuffle(products)
    product_blue = products[0:100]

    pipe = r.pipeline()
    [pipe.sadd('products', x) for x in list_products]
    [pipe.sadd('products:men', x) for x in product_men]
    [pipe.sadd('products:women', x) for x in product_women]
    [pipe.sadd('products:color:blue', x) for x in product_blue]
    pipe.execute()


    print 'INTER EXAMPLE'
    print "========" * 5

    result = r.sinter(['products', 'products:men', 'products:color:blue'])
    print 'total product : %s' % len(result)
    print result

    print '\n' * 4
    print 'INTERSTORE EXAMPLE'
    print "========" * 5
    r.sinterstore('products:men:blue', ['products', 'products:men', 'products:color:blue'])
    result2 = r.sinter(['products:men:blue', 'products', 'products:women', 'products:color:blue'])

    print 'total product : %s' % len(result2)
    print result2


if __name__ == '__main__':
    main()