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
    location.reload();
  }
}
