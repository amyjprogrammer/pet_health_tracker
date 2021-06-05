//creating the random Cat Generator

function randomGenCat(){
  //set up the image
  let catImage = document.createElement('img');
  //grab the id to place the image
  let genCat = document.getElementById('flex-cat-gen');

  catImage.src = 'http://thecatapi.com/api/images/get?format=src&type=gif&size=small';
  catImage.setAttribute('name', 'classCat' );
  genCat.appendChild(catImage);
}

//function to delete the cats
function deleteAllCat(){
  let removeCat = document.getElementsByName('classCat');
  //check for cat images
  while (removeCat.length > 0){
    removeCat[0].parentNode.removeChild(removeCat[0]);
    //reloads the page and resets button
    location.reload();
  }
}

//Cat, Person, Catnip Game (just like rock, paper, scissors)
function playGame(yourChoice){
  let humanChoice = yourChoice.id
  console.log('Human pick:', humanChoice);
  let computerChoice = computerPick(randomNum());
  console.log('Computer pick:', computerChoice);
  let verifyWinner = findWinner(humanChoice, computerChoice);
  console.log(verifyWinner);
  let endMessage = finalMessage(verifyWinner);
  console.log(endMessage);
  finalScreen(humanChoice, computerChoice, endMessage);
}

//computer picking a random number 0, 1, 2
function randomNum(){
  return Math.floor(Math.random() * 3);
}

//computer picking Cat, Person, Catnip
function computerPick(number){
  return ['cat', 'person', 'catnip'][number];
}

//finding the winner
function findWinner(humanChoice, computerChoice){
  let winDatabase = {
    'cat': {'person': 1, 'cat': 0.5, 'catnip': 0},
    'person': {'catnip': 1, 'person': 0.5, 'cat': 0},
    'catnip': {'cat': 1, 'catnip': 0.5, 'person': 0}
  }
  let humanPick = winDatabase[humanChoice][computerChoice];
  let computerPick = winDatabase[computerChoice][humanChoice];

  return [humanPick, computerPick];
}

//display the text on who won
function finalMessage(verifyWinner){
  if (verifyWinner[0] === 1){
    return {'message': 'You won!', 'color': 'green'};
  } else if (verifyWinner[0] === 0.5){
    return {'message': "You tied", 'color':'yellow'};
  } else if (verifyWinner[0] === 0){
    return {'message': 'You lost.', 'color': 'red'};
  }
}

function finalScreen(humanChoice, computerChoice, endMessage){
  //creating a database for the pictures
  var picDatabase = {
    'cat': document.getElementById('cat').src,
    'person': document.getElementById('person').src,
    'catnip': document.getElementById('catnip').src
  }

  //removing all the pictures
  document.getElementById('cat').remove();
  document.getElementById('person').remove();
  document.getElementById('catnip').remove();

  let personDiv = document.createElement('div');
  let catDiv = document.createElement('div');
  let messageDiv = document.createElement('div');

  personDiv.innerHTML = "<img src='" + picDatabase[humanChoice] + "' height=150 width=150 style='box-shadow: 0px 10px 25px rgba(37, 50, 233, 1)'>";
  messageDiv.innerHTML = "<h1 style='color: " + endMessage['color'] + "; font-size: 60px; padding: 30px; '>" + endMessage['message'] + "</h1>";
  catDiv.innerHTML = "<img src='" + picDatabase[computerChoice] + "' height=150 width=150 style='box-shadow: 0px 10px 25px rgba(255, 43, 63)'>";

  document.getElementById('cat-person-catnip').appendChild(personDiv);
  document.getElementById('cat-person-catnip').appendChild(messageDiv);
  document.getElementById('cat-person-catnip').appendChild(catDiv);

  //button to restart the Game
  let btn = document.createElement('button');
  btn.style.backgroundColor='#33cc33';
  btn.innerHTML = 'Replay';
  btn.type = 'submit';
  btn.name = 'Replay';
  btn.onclick = function(){
    location.reload();
  };
  document.getElementById('btn-replay').appendChild(btn);
}
