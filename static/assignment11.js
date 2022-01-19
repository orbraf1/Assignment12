function getUser(){
    const user_id = document.getElementById("frontend_num");
    const full_url = "https://reqres.in/api/users/" + user_id.value;
    console.log(full_url);
    fetch(full_url).then(
        response => response.json()
    ).then((response_obj) => {
        return put_user_inside_html(response_obj.data)
    }
    ).catch(
        err => console.log(err)
    )
}

function put_user_inside_html(response_obj_data) {
    const current_main = document.querySelector("main");
    current_main.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send Email</a>
            <br><br>
        </div>
    `;
}