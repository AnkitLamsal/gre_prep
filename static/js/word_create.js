let family = [];
let wordfamily = [];

window.onload =  function() {
    const select_div = document.getElementById('div_id_family');
    select_div.style.display = 'none';
    const select = select_div.querySelector('select');
    select.required = false;
    const submitButton = document.getElementById('submit-btn');
    select_div.querySelectorAll('option').forEach(option => {
        family.push(option.text);
    });
    const search_bar = document.getElementById('search-bar');
    const search_field = document.createElement('input');
    const search_button = document.createElement('button');
    const search_found  = document.createElement('div');
    const search_not_found  = document.createElement('div');
    search_button.setAttribute('type', 'button');
    search_button.setAttribute('id', 'search-button');
    search_button.setAttribute('class', 'btn btn-primary');
    search_button.innerHTML = 'Search and Add Word Family';
    search_field.setAttribute('type', 'text');
    search_field.setAttribute('id', 'search-field');
    search_field.setAttribute('placeholder', 'Search Families');
    search_found.setAttribute('id', 'search-found');
    search_not_found.setAttribute('id', 'search-not-found');
    search_bar.appendChild(search_field);
    search_bar.appendChild(search_button);
    search_bar.appendChild(search_found);
    search_bar.appendChild(search_not_found);
    search_button.addEventListener('click', handleSearch);
    submitButton.addEventListener('click', submitData);
};

// const request_data = async () =>{
//     response = await fetch('http://127.0.0.1:8000/family/list-json/');
//     data = await response.json();
//     return data;
// };

function handleSearch() {
    const search_field = document.getElementById('search-field');
    const search_value = search_field.value;
    let search_results = null;
    for (let i = 0; i < family.length; i++) {
        if (family[i].toLowerCase() == search_value.toLowerCase()) {
            search_results = family[i];
            break;
        }
    }
    let search_found = document.getElementById('search-found');
    let search_not_found = document.getElementById('search-not-found');
    if(search_results == null){
        console.log("Not Found");
        search_not_found.innerHTML = String(search_value)+ ' is not found';
        // search_found.innerHTML = '';
    }
    else{
        wordfamily.push(search_results);
        search_found.innerHTML = wordfamily + ' added';
        search_not_found.innerHTML = '';
    }
}
let j = 0;
const submitData = () =>{
    const submitButton = document.getElementById('submit-btn');
    submitButton.disabled = true;
    const select = document.getElementById('div_id_family');
    select.querySelectorAll('option').forEach(option => {
        for (let i = 0; i < wordfamily.length; i++) {
            if (option.text == wordfamily[i]) {
                option.selected = true;
                j++;
            }
        }
    });
    console.log(j);
    if (j==0){
        alert('Must add one or word family');
    }
    // select.style.display = 'block';
    submitButton.disabled = false;
};