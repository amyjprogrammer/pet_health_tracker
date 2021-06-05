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
  //let finalScreen = lastScreen(humanChoice, computerChoice, endMessage)
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

//function finalScreen(humanChoice, computerChoice, endMessage){}
