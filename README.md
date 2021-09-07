# mercado-livre-api

find products
## installing on your machine

download the project on github, after that open your terminal and write:

```
$ cd mercado-livre-api
    # enter in the app folder
$ pip install -r requirements.txt
    # install the dependencies
$ python app.py
    # execute the app
```

to stop the server(localhost) press <kbd>Ctrl</kbd><kbd>+</kbd><kbd>C</kbd> or <kbd>Cmd</kbd><kbd>+</kbd><kbd>C</kbd>

# mini-tutorial
***This is an example***

to use the api, use this link: [https://mercado-livre-api-loshad.herokuapp.com/api/find-all/{product}](https://mercado-livre-api-loshad.herokuapp.com/api/find-all/chocolate)
or this link [https://mercado-livre-api-loshad.herokuapp.com/api/find/{product}](https://mercado-livre-api-loshad.herokuapp.com/api/find/chocolate)

### /api/find-all/ returned json
***This is an example***

```
{
  "products": [
    {
      "coin": "R$",
      "id": 0,
      "link": "https://produto.mercadolivre.com.br/MLB-945375944-maxi-chocolate-bauducco-display-c20un-_JM#position=5&search_layout=stack&type=item&tracking_id=dc4917b3-0dd3-4181-8a29-670bf54f519f",
      "name": "Maxi Chocolate Bauducco Display C/20un",
      "price": "15.90"
    },
    {
      "coin": "R$",
      "id": 1,
      "link": "https://produto.mercadolivre.com.br/MLB-1882188964-nestle-chocobiscuit-80g-_JM#position=6&search_layout=stack&type=item&tracking_id=dc4917b3-0dd3-4181-8a29-670bf54f519f",
      "name": "Nestle Chocobiscuit 80g",
      "price": "5.53"
    }
  ],
  "searched_day": "Tuesday, September 07, 2021 20:53:22"
```

### /api/find/ returned json
***This is an example***

```
{
  "product": [
    {
      "coin": "R$",
      "id": 0,
      "link": "https://produto.mercadolivre.com.br/MLB-945375944-maxi-chocolate-bauducco-display-c20un-_JM#position=5&search_layout=stack&type=item&tracking_id=dc4917b3-0dd3-4181-8a29-670bf54f519f",
      "name": "Maxi Chocolate Bauducco Display C/20un",
      "price": "15.90"
    }
  ],
  "searched_day": "Tuesday, September 07, 2021 20:53:22"
```
## License
[MIT](LICENSE)