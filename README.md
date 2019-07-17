

# inventory-backend

## Installation

### Requirements:
Docker must be installed on your machine

- Clone the repo locally

  ```bash
  git clone git@github.com:Omar-kh/inventory-backend.git
  ```

  

- Go into the folder

  ```bash
  cd inventory-backend
  ```

  

- Build the docker container (may take some time, make sure you have an Internet connection):

  ```bash
  sudo docker build -t inventory-backend .
  ```

- Run the container

  ```bash
  sudo docker run -d -p 5000:5000 inventory-backend
  ```

  

**That's it. Your API should be running on your machine on port 5000**

## API Endpoints

The API has two endpoints :

Supposing your are on localhost:

### All products

```
http://localhost:5000/inventory
```

==> Returns a list of products with their ids and names

```json
[

    {
        "product_id": "9f0d518206",
        "product_name": "Product_1"
    },
    {
        "product_id": "6fd7aaa08a",
        "product_name": "Product_2"
    },
    
    ...

]
```



### A product info

```
http://localhost:5000/inventory/${product_id}
```
==> Returns inventory values of the requested product over time

```json
{

    "product_id": "9f0d518206",
    "product_name": "Product_1",
    "dates": [
        "2019-07-01",
        "2019-07-02",
        "2019-07-03",
        "2019-07-04",
        "2019-07-05",
        ...
    ],
    "values": [
        9641,
        181,
        908,
        6536,
        2983,
        ...
    ]

}
```

