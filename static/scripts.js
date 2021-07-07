async function toggleFavTeam(e) {
  e.preventDefault()
  id = $(this).data('team-id')
  req = {
      "team_id": id 
    }
  
  if ($(this).children(":first").hasClass("fas")) {
    let resp = await axios.delete("/user/2/fav_team", { params : req });
    console.log(resp.data)
    if (!resp.data.includes(id)) {
      $(this).children(":first").addClass("far").removeClass("fas")
    }
  } else {
    let resp = await axios.post("/user/2/fav_team", { params: req })
    console.log(resp.data)
    if (resp.data.includes(id)) {
      $(this).children(":first").addClass("fas").removeClass("far")
    }
  }
}

$(".like-team").on("click", toggleFavTeam);