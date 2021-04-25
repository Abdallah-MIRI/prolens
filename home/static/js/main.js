
///////
// Event Load Image
///////
// let catImg = document.querySelectorAll('.cat-img');

// window.onload = () => {
//   catImg.forEach(img => {
//     img.style.display = 'block';
//   })
// }

///////
// Event Load Image
///////
let mainAside = document.getElementById('main-aside');
let creatHeader = document.createElement('header');

if (window.innerWidth <= '600') {
  console.log(window.innerWidth);
  mainAside.insertAdjacentElement = creatHeader;
}

///////
// Event Icon
///////
let body = document.getElementById('body');
let aside = document.getElementById('main-aside');
let iconhamburger = document.getElementById('icon-hamburger');

iconhamburger.addEventListener('click', () => {
  iconhamburger.classList.toggle('active');
  aside.classList.toggle('show');
  body.classList.toggle('hidden');
})

///////
// Get Posts Json
///////
// console.log("Hello world")
// let visible = 3

// $.ajax({
//   type: 'GET',
//   url: `/home/${visible}/`,
//   success: function(response) {
//     // console.log(response)
//     const data = response.data
//     data.map(post=>{
//       console.log(post.id)
//     })
//   },
//   error: function(error) {
//     console.log(error)
//   }
// })

const postsBox = document.getElementById('slide-images')
// const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-more-btn')
const loadBox = document.getElementById('load-box')
let catImg = document.createElement('div')
let catImgAtt = document.createAttribute('class')
let visible = 15
let createTageImg = document.createElement('img')
let createTageDiv = document.createElement('div')

// Add Class List Tages
// createTageImg.src('')
createTageDiv.classList.add(['cat-img', 'infinite-item'])

const handleGetData = () => {
  $.ajax({
    type: 'GET',
    url: `home/${visible}/`,
    success: function(response){
      // console.log(response.max)
      // console.log(response)
      maxSize = response.max
      const data = response.data
      // spinnerBox.classList.remove('not-visible')
      setTimeout( () => {
        // spinnerBox.classList.add('not-visible')
        data.map(post=>{
          // console.log(post.img_post)
          // console.log(post.id)
          // console.log(post)
          // createTageImg.src(`media/${post.img_post}`)
          // createTageImg.alt(`'${post.img_alt}'`)
          // createTageImg.title(`'${post.title}'`)
          // createTageDiv.appendChild(createTageImg)
          // postsBox.appendChild(createTageDiv)
          postsBox.innerHTML += `<div class="cat-img infinite-item grid-item">
                                <img src="media/${post.img_post}" alt="${post.img_alt}" width="100%" height="100%" title="${post.title}" style="display: block;">
                              </div>`
        })
        if (maxSize) {
          console.log('done')
          // loadBtn.classList.add('d-none')
          loadBtn.classList.add('d-none')
          loadBox.innerHTML = `<p class="text-center">No More Posts</p>`
        }
      }, 50)
      
    },
    error: function(error){
      console.log(error)
    }
  })
}
handleGetData()

loadBtn.addEventListener('click', () => {
  visible += 3
  handleGetData()
})