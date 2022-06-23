window.onload = () => {
    fetch("/api/timeline_post").then(data => {
        data.json().then(json => {
            console.log(json.timeline_posts)
            document.getElementById("posts").innerHTML += "<hr>"
            for(postNum in json.timeline_posts) {
                var currentPost = json.timeline_posts[postNum];
                document.getElementById("posts").innerHTML += "<h2>" + currentPost.name + "</h2>"
                document.getElementById("posts").innerHTML += "<h3><a href='mailto:" + currentPost.email + "'>" + currentPost.email + "</a></h3>"
                document.getElementById("posts").innerHTML += "<h3>" + currentPost.created_at + "</h3>"
                document.getElementById("posts").innerHTML += "<p>" + currentPost.content + "</p>"
                document.getElementById("posts").innerHTML += "<hr>"
            }
        })
    })
}

function submitPost() {
    console.log("Submitting post")

    let postData = new FormData()
    postData.append("name", document.getElementById("name").value)
    postData.append("email", document.getElementById("email").value)
    postData.append("content", document.getElementById("content").value)

    fetch("/api/timeline_post", {method: "POST", body: postData}).then((result) => {
        location.reload()
    })
}