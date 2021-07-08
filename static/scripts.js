async function toggleFavTeam(e) {
  e.preventDefault();

  id = $(this).data('team-id');
  user_id = $("body").data('user-id');

  $star = $(this).children(":first");
  req = { "team_id": id };
  
  if ($star.hasClass("fas")) {
    console.log("fas")
    let resp = await axios.delete(`/user/${user_id}/fav_team`, { params: req });
      if (!resp.data.includes(id)) {
        $star.addClass("far").removeClass("fas");
      }
      console.log(resp)
  } else {
    console.log("far")
    let resp = await axios.post(
      `/user/${user_id}/fav_team`, 
      { params: req });
      console.log(resp)
    if (resp.data.includes(id)) {
      $star.addClass("fas").removeClass("far");
    }
  }
}

$(".like-team").on("click", toggleFavTeam);

async function toggleFavPlayer(e) {
  e.preventDefault();

  id = $(this).data("player-id");
  user_id = $("body").data("user-id");

  $star = $(this).children(":first");
  req = { player_id: id };

  if ($star.hasClass("fas")) {
    let resp = await axios.delete(`/user/${user_id}/fav_player`, {
      params: req,
    });
    if (!resp.data.includes(id)) {
      $star.addClass("far").removeClass("fas");
    }
  } else {
    let resp = await axios.post(
      `/user/${user_id}/fav_player`, 
      { params: req });
    if (resp.data.includes(id)) {
      $star.addClass("fas").removeClass("far");
    }
  }
}

$(".like-player").on("click", toggleFavPlayer);