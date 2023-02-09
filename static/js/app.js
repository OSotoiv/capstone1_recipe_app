const $save_recipe = $('#save_recipe')
$save_recipe.on('click', saveRecipe)
const $saved_or_not = $('#saved_or_not')
const recipe_img = $('#recipe_img')
const ingredients_list = document.querySelectorAll('#ingredient')
const BASEURL = 'https://recipes-app-capstone.herokuapp.com'
function sayhi(e) {
    e.preventDefault;
    console.log('hi')
}
async function saveRecipe(e) {
    e.preventDefault();
    const recipe_id = $('#save_recipe').data('recipe_id');
    const recipe_title = $('#save_recipe').data('recipe_title');
    const ingredients_text = [];
    ingredients_list.forEach((item) => ingredients_text.push(item.innerText))
    try {
        const res = await axios({
            url: `${BASEURL}/${recipe_id}/${recipe_title}`,
            method: "POST",
            data: { ingredients: ingredients_text, image: recipe_img[0].src }
        })
        if (res.data.response == 'unsaved') {
            $('#save_recipe').remove()
            $save_icon = $(`<button data-recipe_id=${recipe_id}
                            data-recipe_title=${recipe_title}
                            id="save_recipe" 
                            class="btn btn-primary btn-sm">
                            <i class="fa-regular fa-bookmark">
                            </i>Save to Cookbook</button>`)
            $save_icon.on('click', saveRecipe)
            $saved_or_not.append($save_icon)
        }
        else if (res.data.response == 'saved') {
            $('#save_recipe').remove()
            $save_icon = $(`<button data-recipe_id=${recipe_id}
                            data-recipe_title=${recipe_title}
                            id="save_recipe" 
                            class="btn btn-secondary btn-sm">
                            <i class="fa-solid fa-bookmark">
                            </i> SAVED</button>`)
            $save_icon.on('click', saveRecipe)
            $saved_or_not.append($save_icon)
        }
    } catch (error) {
        console.log(error)
    }
}

const $recipes_view = $('#recipes_view')
const $more_button = $('#more')
$more_button.on('click', get_more_random_recipes)

async function get_more_random_recipes(e) {
    e.preventDefault()
    // check scroll location for the bottom of the page.
    // if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
    //     console.log('bottom reached')
    // make the API call
    const res = await axios({
        url: `${BASEURL}/search/random/more`,
        method: "GET",
    })
    $recipes_view.append(res.data)
    // }
};

// $(window).scroll(get_more_random_recipes);