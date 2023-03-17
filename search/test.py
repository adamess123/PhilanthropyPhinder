import search


def main():
    street = '11742 NW 57th Street'
    city = 'Coral Springs'
    state = 'FL'
    zip = '33076'
    category = 'X'
    res = search.search(street, city, zip, category)
    top_100 = res.head(100)
    if res is None:
        print('error')
    else:
        print(top_100.head())


if __name__ == '__main__':
    main()
