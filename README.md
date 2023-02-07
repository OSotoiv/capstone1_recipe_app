# Recipe Finder

Recipe Finder is a web application built using Python and Flask that allows users to search for recipes, save their favorite recipes in a personal cookbook. The recipes all come from [spoonacularAPI](https://spoonacular.com/food-api)

## Features

- Sign up with unique email and username
- Search for recipes by ingredients
- Search for a random recipe
- View the top 5 most saved recipes by other users
- Save recipes to a personal cookbook
- Create and share your own recipes

## Getting Started

1. Clone the repository
```git clone https://github.com/OSotoiv/capstone1_recipe_app.git```
or
```gh repo clone OSotoiv/capstone1_recipe_app```

2. Install the dependencies
```pip install -r requirements.txt```


3. Run the application
```export FLASK_APP=app```
```flask run```

4. Note that you will need to set your own env_keys folder.
APP_CONFIG_KEY = 'secretkey'

API_KEY = 'sign up with Spoonacular to get your API KEY'

BLOB_NAME = 'sign up with Azuer to get a blob name'

BLOB_KEY = 'sign up with Azuer to get a blob key'

BLOB_STRING = 'sign up with Azuer to get a blob string'

BLOB_CONTAINER_NAME = 'sign up with Azuer to get a blob container name'

If you dont want to user Azuer you can also save files localy with ```Image_from_WTForm.save(os.path.join(UPLOAD_FOLDER, img_name))```
If you are unsure how to do this just ask ChatGPT :sunglasses:

1. Visit [http://localhost:5000](http://localhost:5000) to use the application.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make the necessary changes
4. Create a pull request

## Support

If you have any questions or run into any issues, feel free to reach out to me at [Osoto.iv@gmail.com]().


## Comming soon....
1. Testing...
2. Users functionality for creating your own recipes.
3. Comments on users recipes.